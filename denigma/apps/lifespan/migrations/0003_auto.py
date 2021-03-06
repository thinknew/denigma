# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field type on 'Manipulation'
        db.delete_table('lifespan_manipulation_type')


    def backwards(self, orm):
        # Adding M2M table for field type on 'Manipulation'
        db.create_table('lifespan_manipulation_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_manipulation', models.ForeignKey(orm['lifespan.manipulation'], null=False)),
            ('to_manipulation', models.ForeignKey(orm['lifespan.manipulation'], null=False))
        ))
        db.create_unique('lifespan_manipulation_type', ['from_manipulation_id', 'to_manipulation_id'])


    models = {
        'annotations.animal': {
            'Meta': {'object_name': 'Animal'},
            'alternative_names': ('django.db.models.fields.CharField', [], {'max_length': '21', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'annotations.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'annotations.species': {
            'Meta': {'object_name': 'Species'},
            'alternative_names': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['annotations.Animal']", 'symmetrical': 'False'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'gendr_genes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gendr_orthologs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gendr_paralogs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'latin_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'latin_shortcut': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'number_genes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'datasets.reference': {
            'Meta': {'object_name': 'Reference', 'db_table': "u'reference'"},
            'access_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'accession_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alternate_journal': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'article_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author_address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'authors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'call_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'database_provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'epub_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'legal_note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name_of_database': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nihmsid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'original_publication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'pmcid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pmid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reprint_editione': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'research_notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reviewed_itemse': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'start_page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'translated_author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'type_of_article': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lifespan.assay': {
            'Meta': {'object_name': 'Assay'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lifespan.comparision': {
            'Meta': {'object_name': 'Comparision'},
            'control': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'control_group'", 'to': "orm['lifespan.Measurement']"}),
            'epistasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifespan.Epistasis']", 'null': 'True', 'blank': 'True'}),
            'experimental': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'experimental_group'", 'to': "orm['lifespan.Measurement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervention': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifespan.Intervention']", 'null': 'True', 'blank': 'True'}),
            'max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'median': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'lifespan.epistasis': {
            'Meta': {'object_name': 'Epistasis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lifespan.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['annotations.Species']"}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifespan.Study']"})
        },
        'lifespan.factor': {
            'Meta': {'object_name': 'Factor'},
            '_25': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            '_75': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '270', 'blank': 'True'}),
            'antagonistic_epistasis': ('django.db.models.fields.CharField', [], {'max_length': '216', 'blank': 'True'}),
            'assay': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Assay']", 'symmetrical': 'False'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'classifications': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['annotations.Classification']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'diet_regimen': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'functional_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gene_intervention': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'human_homologue': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervention': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Intervention']", 'symmetrical': 'False', 'blank': 'True'}),
            'life_span': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'manipulation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maximum': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'mean': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'median': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '244', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pubmed_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['datasets.Reference']", 'symmetrical': 'False', 'blank': 'True'}),
            'regimen': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Regimen']", 'symmetrical': 'False', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'synergistic_epistasis': ('django.db.models.fields.CharField', [], {'max_length': '33', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Type']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'lifespan.intervention': {
            'Meta': {'object_name': 'Intervention'},
            '_25': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            '_75': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'background': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'effect': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifespans': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'manipulation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Manipulation']", 'symmetrical': 'False', 'blank': 'True'}),
            'maximum': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'mean': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'median': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pmid': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['datasets.Reference']", 'symmetrical': 'False', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lifespan.manipulation': {
            'Meta': {'object_name': 'Manipulation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'lifespan.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'comparisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Measurement']", 'through': "orm['lifespan.Comparision']", 'symmetrical': 'False'}),
            'control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifespan.Experiment']"}),
            'genotype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'median': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'strain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifespan.Strain']", 'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'lifespan.regimen': {
            'Meta': {'object_name': 'Regimen'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lifespan.strain': {
            'Meta': {'object_name': 'Strain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'lifespan.study': {
            'Meta': {'object_name': 'Study'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integrated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pmid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Reference']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'lifespan.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['lifespan']