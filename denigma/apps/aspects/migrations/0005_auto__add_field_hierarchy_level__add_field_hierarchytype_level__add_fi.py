# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Hierarchy.level'
        db.add_column('aspects_hierarchy', 'level',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'HierarchyType.level'
        db.add_column('aspects_hierarchytype', 'level',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Language.level'
        db.add_column('aspects_language', 'level',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Hierarchy.level'
        db.delete_column('aspects_hierarchy', 'level')

        # Deleting field 'HierarchyType.level'
        db.delete_column('aspects_hierarchytype', 'level')

        # Deleting field 'Language.level'
        db.delete_column('aspects_language', 'level')


    models = {
        'aspects.grade': {
            'Meta': {'object_name': 'Grade', '_ormbases': ['aspects.Hierarchy']},
            'hierarchy_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['aspects.Hierarchy']", 'unique': 'True', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aspects.Language']", 'null': 'True', 'blank': 'True'})
        },
        'aspects.hierarchy': {
            'Meta': {'object_name': 'Hierarchy'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'requirement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Image']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aspects.HierarchyType']", 'null': 'True', 'blank': 'True'})
        },
        'aspects.hierarchytype': {
            'Meta': {'object_name': 'HierarchyType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'requirement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Image']", 'null': 'True', 'blank': 'True'})
        },
        'aspects.language': {
            'Meta': {'object_name': 'Language'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'requirement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Image']", 'null': 'True', 'blank': 'True'})
        },
        'aspects.rank': {
            'Meta': {'object_name': 'Rank', '_ormbases': ['aspects.Hierarchy']},
            'hierarchy_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['aspects.Hierarchy']", 'unique': 'True', 'primary_key': 'True'})
        },
        'aspects.role': {
            'Meta': {'object_name': 'Role', '_ormbases': ['aspects.Hierarchy']},
            'hierarchy_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['aspects.Hierarchy']", 'unique': 'True', 'primary_key': 'True'})
        },
        'aspects.title': {
            'Meta': {'object_name': 'Title', '_ormbases': ['aspects.Hierarchy']},
            'hierarchy_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['aspects.Hierarchy']", 'unique': 'True', 'primary_key': 'True'})
        },
        'media.photourl': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['aspects']