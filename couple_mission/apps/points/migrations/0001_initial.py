# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Points'
        db.create_table('points', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UaiUser'])),
            ('couple', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.Couple'])),
            ('couple_mission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['couple.CoupleMission'])),
            ('points', self.gf('django.db.models.fields.IntegerField')(default='0')),
        ))
        db.send_create_signal(u'points', ['Points'])


    def backwards(self, orm):
        # Deleting model 'Points'
        db.delete_table('points')


    models = {
        u'account.uaiuser': {
            'Meta': {'object_name': 'UaiUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
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
        },
        u'couple.couplemission': {
            'Meta': {'object_name': 'CoupleMission', 'db_table': "'couple_mission'"},
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['uai.Mission']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'points.points': {
            'Meta': {'object_name': 'Points', 'db_table': "'points'"},
            'couple': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.Couple']"}),
            'couple_mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['couple.CoupleMission']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.UaiUser']"})
        },
        u'uai.mission': {
            'Meta': {'object_name': 'Mission'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['uai.MissionCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'uai.missioncategory': {
            'Meta': {'object_name': 'MissionCategory', 'db_table': "'uai_mission_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['points']