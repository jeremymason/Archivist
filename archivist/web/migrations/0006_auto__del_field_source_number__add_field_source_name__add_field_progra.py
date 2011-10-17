# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Source.number'
        db.delete_column('web_source', 'number')

        # Adding field 'Source.name'
        db.add_column('web_source', 'name', self.gf('django.db.models.fields.CharField')(default='NAME', max_length=100), keep_default=False)

        # Adding field 'Program.digitized'
        db.add_column('web_program', 'digitized', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Genre.source'
        db.delete_column('web_genre', 'source')

        # Deleting field 'Subject.source'
        db.delete_column('web_subject', 'source')


    def backwards(self, orm):
        
        # Adding field 'Source.number'
        db.add_column('web_source', 'number', self.gf('django.db.models.fields.CharField')(default=0, max_length=50), keep_default=False)

        # Deleting field 'Source.name'
        db.delete_column('web_source', 'name')

        # Deleting field 'Program.digitized'
        db.delete_column('web_program', 'digitized')

        # Adding field 'Genre.source'
        db.add_column('web_genre', 'source', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True), keep_default=False)

        # Adding field 'Subject.source'
        db.add_column('web_subject', 'source', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True), keep_default=False)


    models = {
        'web.digitalfile': {
            'Meta': {'object_name': 'DigitalFile'},
            'bit_depth': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'date_digitized': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['web.Program']", 'unique': 'True'}),
            'sample_rate': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'tracks': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'who_digitized': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Person']", 'through': "orm['web.DigitalFileParticipant']", 'symmetrical': 'False'})
        },
        'web.digitalfilelocation': {
            'Meta': {'object_name': 'DigitalFileLocation'},
            'digital_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.DigitalFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'web.digitalfileparticipant': {
            'Meta': {'unique_together': "(('role', 'digital_file'),)", 'object_name': 'DigitalFileParticipant'},
            'digital_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.DigitalFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Role']"})
        },
        'web.genre': {
            'Meta': {'ordering': "['genre']", 'object_name': 'Genre'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'web.person': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.program': {
            'Meta': {'ordering': "['title']", 'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'digitized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'first_broadcast': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'member_of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Series']", 'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Person']", 'through': "orm['web.ProgramParticipant']", 'symmetrical': 'False'}),
            'rights': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Rights']", 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Source']"}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Subject']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'web.programparticipant': {
            'Meta': {'object_name': 'ProgramParticipant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Person']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Program']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Role']"})
        },
        'web.rights': {
            'Meta': {'object_name': 'Rights'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'right_type_source': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'web.role': {
            'Meta': {'object_name': 'Role'},
            'applies_to': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'web.series': {
            'Meta': {'ordering': "['name']", 'object_name': 'Series'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'web.seriesparticipant': {
            'Meta': {'object_name': 'SeriesParticipant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Role']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Series']"})
        },
        'web.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.SourceFormat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.SourceLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recorded_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tracks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'web.sourceformat': {
            'Meta': {'ordering': "['name']", 'object_name': 'SourceFormat'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'web.sourcelocation': {
            'Meta': {'ordering': "['location']", 'object_name': 'SourceLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'web.sourceparticipant': {
            'Meta': {'object_name': 'SourceParticipant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Role']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Source']"})
        },
        'web.subject': {
            'Meta': {'ordering': "['subject']", 'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['web']
