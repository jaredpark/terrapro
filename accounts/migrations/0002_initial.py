# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table('accounts_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(unique=True, to=orm['auth.User'])),
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, default='', blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=80, null=True, default='', blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, default='', blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('accounts', ['Organization'])

        # Adding model 'Property'
        db.create_table('accounts_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Organization'], related_name='Properties')),
            ('property_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('property_contact', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('property_phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, default='', blank=True)),
            ('property_email', self.gf('django.db.models.fields.EmailField')(max_length=80, null=True, default='', blank=True)),
            ('property_address', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('property_city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('property_state', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('property_zipcode', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, default='', blank=True)),
            ('property_notes', self.gf('django.db.models.fields.TextField')(max_length=400, null=True, default='', blank=True)),
        ))
        db.send_create_signal('accounts', ['Property'])

        # Adding model 'Contact'
        db.create_table('accounts_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Organization'], related_name='Contacts')),
            ('contact_property', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.Property'], related_name='Properties', blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, default='', blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=80, null=True, default='', blank=True)),
            ('contact_address', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('contact_city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('contact_state', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, default='', blank=True)),
            ('contact_zipcode', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, default='', blank=True)),
            ('contact_notes', self.gf('django.db.models.fields.TextField')(max_length=400, null=True, default='', blank=True)),
        ))
        db.send_create_signal('accounts', ['Contact'])

        # Adding model 'PropertyReport'
        db.create_table('accounts_propertyreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Property'], related_name='Reports')),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=400, null=True, default='', blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('accounts', ['PropertyReport'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('accounts_organization')

        # Deleting model 'Property'
        db.delete_table('accounts_property')

        # Deleting model 'Contact'
        db.delete_table('accounts_contact')

        # Deleting model 'PropertyReport'
        db.delete_table('accounts_propertyreport')


    models = {
        'accounts.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_property': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['accounts.Property']", 'related_name': "'Properties'", 'blank': 'True'}),
            'contact_state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'contact_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Organization']", 'related_name': "'Contacts'"})
        },
        'accounts.organization': {
            'Meta': {'object_name': 'Organization'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'default': "''", 'blank': 'True'})
        },
        'accounts.property': {
            'Meta': {'object_name': 'Property'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Organization']", 'related_name': "'Properties'"}),
            'property_address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_contact': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'property_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'default': "''", 'blank': 'True'})
        },
        'accounts.propertyreport': {
            'Meta': {'object_name': 'PropertyReport'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'report_property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Property']", 'related_name': "'Reports'"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']