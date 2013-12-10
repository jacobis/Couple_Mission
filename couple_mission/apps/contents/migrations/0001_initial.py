# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CommentManager'
        db.create_table('comment_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'contents', ['CommentManager'])

        # Adding model 'Comment'
        db.create_table('contents_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment_manager', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['contents.CommentManager'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='has_comments', to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'contents', ['Comment'])

        # Adding model 'PhotoAlbum'
        db.create_table('contents_photo_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_albums', to=orm['couple.Couple'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'contents', ['PhotoAlbum'])

        # Adding model 'Photo'
        db.create_table('contents_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('comment_manager', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contents.CommentManager'], unique=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['contents.PhotoAlbum'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['contents.Comment'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal(u'contents', ['Photo'])

        # Adding model 'Letter'
        db.create_table('contents_letter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('comment_manager', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contents.CommentManager'], unique=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('reading', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'contents', ['Letter'])


    def backwards(self, orm):
        # Deleting model 'CommentManager'
        db.delete_table('comment_manager')

        # Deleting model 'Comment'
        db.delete_table('contents_comment')

        # Deleting model 'PhotoAlbum'
        db.delete_table('contents_photo_album')

        # Deleting model 'Photo'
        db.delete_table('contents_photo')

        # Deleting model 'Letter'
        db.delete_table('contents_letter')


    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contents.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['contents.CommentManager']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'has_comments'", 'to': u"orm['auth.User']"})
        },
        u'contents.commentmanager': {
            'Meta': {'object_name': 'CommentManager', 'db_table': "'comment_manager'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contents.letter': {
            'Meta': {'object_name': 'Letter'},
            'comment_manager': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.CommentManager']", 'unique': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reading': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contents.photo': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['contents.PhotoAlbum']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['contents.Comment']", 'null': 'True', 'blank': 'True'}),
            'comment_manager': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.CommentManager']", 'unique': 'True'}),
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contents.photoalbum': {
            'Meta': {'object_name': 'PhotoAlbum', 'db_table': "'contents_photo_album'"},
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo_albums'", 'to': u"orm['couple.Couple']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'couple.couple': {
            'Meta': {'unique_together': "(('partner_a', 'partner_b'),)", 'object_name': 'Couple', 'db_table': "'couple'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner_a': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partner_a'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'partner_b': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partner_b'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contents']