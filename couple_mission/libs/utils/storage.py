import StringIO
import mimetypes
import datetime

from dateutil import parser

from os.path import join, normpath

from django.core.files import File
from django.core.files.storage import Storage
from django.conf import settings
from django.utils import timezone

from azure.storage import BlobService, WindowsAzureMissingResourceError, TableService, Entity


class AzureBlobStorage(Storage):

    '''
    classdocs
    '''

    def __init__(self, azure_profile):
        '''
        Constructor
        '''

        if not azure_profile:
            raise Exception()
        else:
            container_name = azure_profile['container_name']
            account_name = azure_profile['account_name']
            account_key = azure_profile['key']
            base_url = azure_profile['base_url']

        self.blob = BlobService(
            account_name=account_name, account_key=account_key)

        self.container = container_name
        self.base_url = base_url

    def delete(self, name):
        """
        Delete file.
        """
        try:
            self.blob.delete_blob(self.container, name)
        except WindowsAzureMissingResourceError:
            return False
        else:
            return True

    def delete_files(self, files=None):
        """
        Delete files in container.
        """
        if not files:
            files = self.listdir(self.container)[1]

        for _file in files:
            self.delete(_file)

    def exists(self, name, with_properties=False):
        """
        Existing check.
        """
        result = False
        blob_properties = None

        try:
            blob_properties = self.blob.get_blob_properties(
                self.container, name)
        except WindowsAzureMissingResourceError:
            result = False
        else:
            result = True

        if with_properties:
            return result, blob_properties
        else:
            return result

    def get_available_name(self, name):
        return super(AzureBlobStorage, self).get_available_name(name.replace('\\', '/'))

    def get_valid_name(self, name):

        return name

    def _list(self, path, prefix, maxresults):
        result = []
        blobs = self.blob.list_blobs(path, prefix, maxresults)

        for _blob in blobs:
            result.append(_blob.name)

        return result

    def listdir(self, path=None, prefix=None, maxresults=None):
        """
        Catalog file list.
        """
        if not path:
            path = self.container
        return [], self._list(path, prefix, maxresults)

    def size(self, name):
        """
        File size.
        """

        result, properties = self.exists(name, with_properties=True)

        if result:
            return int(properties['content-length'])
        else:
            return 0

    def url(self, name, chk_exist=False):
        """
        URL for file downloading.
        """

        if chk_exist:
            if self.exists(name):
                return '%s%s/%s' % (self.base_url, self.container, name)
            else:
                return None
        else:
            return '%s%s/%s' % (self.base_url, self.container, name)

    def _open(self, name, mode='rb'):
        """
        Open file.
        """

        in_mem_file = StringIO.StringIO(
            self.blob.get_blob(self.container, name))
        in_mem_file.name = name
        in_mem_file.mode = mode
        return File(in_mem_file)

    def _save(self, name, blob_to_upload, x_ms_blob_type='BlockBlob', content_type=None):
        """
        Save file.
        """

        if hasattr(blob_to_upload, 'content_type'):
            content_type = blob_to_upload.content_type or None

        if content_type is None:
            content_type = mimetypes.guess_type(name)[0] or None

        blob_to_upload.seek(0)

        self.blob.put_blob(self.container, name, blob_to_upload,
                           x_ms_blob_type, x_ms_blob_content_type=content_type)

        return name

    def modified_time(self, name):
        """
        Last modification time.
        """

        result, properties = self.exists(name, with_properties=True)

        if result:
            date_string = properties['last-modified']
            modified_dt = parser.parse(date_string)

            if timezone.is_naive(modified_dt):
                return modified_dt
            else:
                return timezone.make_naive(modified_dt, timezone.get_current_timezone())
        else:
            return None

    created_time = accessed_time = modified_time


def get_azure_profile(account_type, container):

    if account_type == 'contents':
        return {'account_name': settings.AZURE_CONTENTS_ACCOUNT_NAME,
                'key': settings.AZURE_CONTENTS_ACCOUNT_KEY,
                'container_name': container,
                'base_url': settings.CONTENTS_BASE_URL,
                'full_url': '%s%s/' % (settings.CONTENTS_BASE_URL, container),
                }

    else:
        raise Exception()


def getfilesystem(container_type):
    from django.core.files.storage import FileSystemStorage

    if container_type in ['usercontents', 'admincontents']:
        if settings.CLOUD_FILESYSTEM:
            file_system_storage = AzureBlobStorage(
                get_azure_profile('contents', container_type))
        else:
            file_system_storage = FileSystemStorage(
                normpath(join(settings.MEDIA_ROOT, container_type)))
    else:
        raise Exception()

    return file_system_storage
