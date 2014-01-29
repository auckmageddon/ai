# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BarTab'
        db.delete_table(u'intranet_bartab')

        # Deleting model 'Entry'
        db.delete_table(u'intranet_entry')

        # Deleting model 'FAQ'
        db.delete_table(u'intranet_faq')

        # Deleting model 'Server'
        db.delete_table(u'intranet_server')

        # Adding model 'Profile'
        db.create_table(u'intranet_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('steam_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('avatar_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('profile_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('game_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('game_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('game_ip', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'intranet', ['Profile'])

        # Adding model 'Article'
        db.create_table(u'intranet_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('frontpage_me', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('entered_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('entered_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'intranet', ['Article'])


    def backwards(self, orm):
        # Adding model 'BarTab'
        db.create_table(u'intranet_bartab', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True)),
            ('claimant', self.gf('django.db.models.fields.CharField')(default='', max_length=15)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('confirmation', self.gf('django.db.models.fields.CharField')(max_length=8, unique=True)),
            ('claimed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('intranet', ['BarTab'])

        # Adding model 'Entry'
        db.create_table(u'intranet_entry', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('entered_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('frontpage_me', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('entered_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('intranet', ['Entry'])

        # Adding model 'FAQ'
        db.create_table(u'intranet_faq', (
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('intranet', ['FAQ'])

        # Adding model 'Server'
        db.create_table(u'intranet_server', (
            ('players', self.gf('django.db.models.fields.IntegerField')()),
            ('game', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('map_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('max_players', self.gf('django.db.models.fields.IntegerField')()),
            ('is_permanent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('intranet', ['Server'])

        # Deleting model 'Profile'
        db.delete_table(u'intranet_profile')

        # Deleting model 'Article'
        db.delete_table(u'intranet_article')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'intranet.article': {
            'Meta': {'ordering': "['-entered_on']", 'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'entered_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'entered_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'frontpage_me': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'intranet.event': {
            'Meta': {'ordering': "['happening_at']", 'object_name': 'Event'},
            'happening_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'intranet.profile': {
            'Meta': {'object_name': 'Profile'},
            'avatar_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'game_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game_ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'steam_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'intranet.tournament': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tournament'},
            'challonge_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scheduled_for': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['intranet.Event']"})
        }
    }

    complete_apps = ['intranet']