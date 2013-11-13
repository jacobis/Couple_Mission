from os.path import join, normpath

from django.conf import settings


def getfilesystem():
    from django.core.files.storage import FileSystemStorage
    
    file_system_storage = FileSystemStorage(normpath(settings.MEDIA_ROOT))

    return file_system_storage