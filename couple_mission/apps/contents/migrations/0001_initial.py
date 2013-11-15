# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table('contents_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UaiUser'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'contents', ['Comment'])

        # Adding model 'PhotoAlbum'
        db.create_table('contents_photo_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'contents', ['PhotoAlbum'])

        # Adding model 'Photo'
        db.create_table('contents_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UaiUser'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.PhotoAlbum'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Comment'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal(u'contents', ['Photo'])

        # Adding model 'Letter'
        db.create_table('contents_letter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UaiUser'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('reading', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'contents', ['Letter'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table('contents_comment')

        # Deleting model 'PhotoAlbum'
        db.delete_table('contents_photo_album')

        # Deleting model 'Photo'
        db.delete_table('contents_photo')

        # Deleting model 'Letter'
        db.delete_table('contents_letter')


    models = {
        u'account.uaiuser': {
            'Meta': {'object_name': 'UaiUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contents.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.UaiUser']"})
        },
        u'contents.letter': {
            'Meta': {'object_name': 'Letter'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reading': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.UaiUser']"})
        },
        u'contents.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contents.PhotoAlbum']"}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contents.Comment']"}),
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.UaiUser']"})
        },
        u'contents.photoalbum': {
            'Meta': {'object_name': 'PhotoAlbum', 'db_table': "'contents_photo_album'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'couple.couple': {
            'Meta': {'unique_together': "(('male', 'female'),)", 'object_name': 'Couple', 'db_table': "'couple'"},
            'female': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'female_from'", 'null': 'True', 'to': u"orm['account.UaiUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'male_from'", 'null': 'True', 'to': u"orm['account.UaiUser']"})
        }
    }

    complete_apps = ['contents']