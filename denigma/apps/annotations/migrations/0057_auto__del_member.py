# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'member'
        db.delete_table('annotations_member')


    def backwards(self, orm):
        
        # Adding model 'member'
        db.create_table('annotations_member', (
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('chr_end', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('stable_id', self.gf('django.db.models.fields.CharField')(max_length=19)),
            ('member_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('Mapping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('chr_start', self.gf('django.db.models.fields.IntegerField')()),
            ('sequence_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('display_label', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('genome_db_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('chr_strand', self.gf('django.db.models.fields.IntegerField')()),
            ('gene_member_id', self.gf('django.db.models.fields.IntegerField')()),
            ('taxon_id', self.gf('django.db.models.fields.IntegerField')()),
            ('entrez_gene_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('chr_name', self.gf('django.db.models.fields.CharField')(max_length=27)),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=17)),
        ))
        db.send_create_signal('annotations', ['member'])


    models = {
        'annotations.animal': {
            'Meta': {'object_name': 'Animal'},
            'alternative_names': ('django.db.models.fields.CharField', [], {'max_length': '21', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'annotations.blog': {
            'Meta': {'object_name': 'Blog'},
            'entry': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['annotations.Entry']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'annotations.candidate': {
            'Meta': {'object_name': 'Candidate', 'db_table': "u'Candidate'"},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {}),
            'fly_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'fly_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'gene_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'human_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'human_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mouse_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'mouse_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'p-Value'", 'blank': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rat_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'rat_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            's': ('django.db.models.fields.IntegerField', [], {}),
            'seed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'specificity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            't': ('django.db.models.fields.IntegerField', [], {}),
            'taxid': ('django.db.models.fields.IntegerField', [], {}),
            'worm_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'worm_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'yeast_homolog_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'yeast_homolog_symbol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'})
        },
        'annotations.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'annotations.discontinuedid': {
            'Meta': {'object_name': 'DiscontinuedId'},
            'discontinued_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.ensemblentrezgeneid': {
            'Meta': {'object_name': 'EnsemblEntrezGeneId'},
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.ensemblhomolog': {
            'Meta': {'object_name': 'EnsemblHomolog'},
            'dn': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'ds': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'ensembl_gene_id_a': ('django.db.models.fields.CharField', [], {'max_length': '18', 'db_index': 'True'}),
            'ensembl_gene_id_b': ('django.db.models.fields.CharField', [], {'max_length': '18', 'db_index': 'True'}),
            'homology_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage_identity_a': ('django.db.models.fields.IntegerField', [], {}),
            'percentage_identity_b': ('django.db.models.fields.IntegerField', [], {}),
            'potential_homolog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'taxid_a': ('django.db.models.fields.IntegerField', [], {}),
            'taxid_b': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.entrez': {
            'Meta': {'object_name': 'Entrez'},
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'full_name_from_nomenclature_autority': ('django.db.models.fields.CharField', [], {'max_length': '251', 'blank': 'True'}),
            'gene_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'hgnc': ('django.db.models.fields.IntegerField', [], {}),
            'hprd': ('django.db.models.fields.IntegerField', [], {}),
            'imgt_gene_db': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'locus_tag': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'mgi': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'mim': ('django.db.models.fields.IntegerField', [], {}),
            'mirbase': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'ratmap': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rgd': ('django.db.models.fields.IntegerField', [], {}),
            'symbol_from_nomeclature_authority': ('django.db.models.fields.CharField', [], {'max_length': '29', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {}),
            'wormbase_id': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'})
        },
        'annotations.entrez_gene': {
            'Meta': {'object_name': 'Entrez_Gene'},
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'full_name_from_nomenclature_autority': ('django.db.models.fields.CharField', [], {'max_length': '251', 'blank': 'True'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'hgnc': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'hprd': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'imgt_gene_db': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'locus_tag': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'mgi': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'mim': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'mirbase': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'ratmap': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rgd': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'symbol_from_nomenclature_authority': ('django.db.models.fields.CharField', [], {'max_length': '29', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {}),
            'wormbase_id': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'})
        },
        'annotations.entry': {
            'Meta': {'object_name': 'Entry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'annotations.gen': {
            'Meta': {'object_name': 'Gen'},
            'ageing_associated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ageing_differential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ageing_induced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ageing_methylated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ageing_suppressed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ageing_suppressor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'circadian_differential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'clock_modulator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clock_modulator_ortholog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clock_systemic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'core_clock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dr_differential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dr_essential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dr_essential_ortholog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dr_induced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dr_suppressed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'embryonic_lethal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '173', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'gerontogene': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'high_amplitude': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'imprinted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'juvenile_associated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'juvenile_differential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'juvenile_induced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'juvenile_suppressed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'long_period': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'longevity_associated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'maternal_imprinted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'negative_ageing_suppressor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'negative_gerontogene': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pacemaker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paternal_imprinted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'positive_ageing_suppressor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'positive_gerontogene': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'senescence_differential': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'senescence_induced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'senescence_suppressed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_period': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {}),
            'transcription_factor': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'annotations.gene': {
            'Meta': {'object_name': 'Gene'},
            'classes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'classification': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['annotations.Classification']", 'symmetrical': 'False'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.gene2ensembl': {
            'Meta': {'object_name': 'gene2ensembl'},
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'db_index': 'True'}),
            'ensembl_protein_id': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'ensembl_rna_id': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein_accession': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'rna_nucleotide_accession': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'annotations.go': {
            'Meta': {'object_name': 'GO'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {}),
            'evidence': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'go_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'go_term': ('django.db.models.fields.CharField', [], {'max_length': '193'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pmid': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.homologene': {
            'Meta': {'object_name': 'HomoloGene'},
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'hid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein_accession': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'protein_gi': ('django.db.models.fields.IntegerField', [], {}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.inparanoid': {
            'Meta': {'object_name': 'InParanoid'},
            'ensembl_gene_id_a': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ensembl_gene_id_b': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'group_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxid_a': ('django.db.models.fields.IntegerField', [], {}),
            'taxid_b': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.ortholog': {
            'Meta': {'object_name': 'Ortholog'},
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'gene_taxid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ortholog': ('django.db.models.fields.IntegerField', [], {}),
            'ortholog_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ortholog_taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'annotations.sgd_features': {
            'Meta': {'object_name': 'SGD_features'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'chromosome': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'coordinate_version': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'feature_qualifier': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'}),
            'feature_type': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'genetic_position': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_feature_name': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'secondary_sgd_id': ('django.db.models.fields.CharField', [], {'max_length': '54', 'blank': 'True'}),
            'sequence_version': ('django.db.models.fields.CharField', [], {'max_length': '43'}),
            'sgd_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_coordinate': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'stop_coordinate': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'strand': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'annotations.sgd_gene_association': {
            'Meta': {'object_name': 'SGD_gene_association'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'date': ('django.db.models.fields.IntegerField', [], {}),
            'evidence': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'go_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orf': ('django.db.models.fields.CharField', [], {'max_length': '54'}),
            'other_ids': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sgd_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'with_or_from': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
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
        }
    }

    complete_apps = ['annotations']
