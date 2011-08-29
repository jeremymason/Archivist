# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DigitalFileLocation'
        db.create_table('web_digitalfilelocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('digital_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.DigitalFile'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('web', ['DigitalFileLocation'])

        # Adding model 'DigitalFile'
        db.create_table('web_digitalfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Program'], unique=True)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sample_rate', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('bit_depth', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('tracks', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('date_digitized', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('web', ['DigitalFile'])

        # Adding model 'SourceLocation'
        db.create_table('web_sourcelocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('web', ['SourceLocation'])

        # Adding model 'SourceFormat'
        db.create_table('web_sourceformat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('web', ['SourceFormat'])

        # Adding model 'Source'
        db.create_table('web_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.SourceLocation'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.SourceFormat'], blank=True)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('tracks', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('recorded_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('web', ['Source'])

        # Adding model 'Series'
        db.create_table('web_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('web', ['Series'])

        # Adding model 'Rights'
        db.create_table('web_rights', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('right_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('right_type_source', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('web', ['Rights'])

        # Adding model 'Genre'
        db.create_table('web_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('web', ['Genre'])

        # Adding model 'Subject'
        db.create_table('web_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('web', ['Subject'])

        # Adding model 'Person'
        db.create_table('web_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('web', ['Person'])

        # Adding model 'Role'
        db.create_table('web_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('applies_to', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('web', ['Role'])

        # Adding model 'Program'
        db.create_table('web_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ident', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Genre'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Source'])),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('first_broadcast', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('member_of', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Series'], blank=True)),
            ('rights', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Rights'], blank=True)),
        ))
        db.send_create_signal('web', ['Program'])

        # Adding M2M table for field subjects on 'Program'
        db.create_table('web_program_subjects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm['web.program'], null=False)),
            ('subject', models.ForeignKey(orm['web.subject'], null=False))
        ))
        db.create_unique('web_program_subjects', ['program_id', 'subject_id'])

        # Adding model 'ProgramParticipant'
        db.create_table('web_programparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Role'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Program'])),
        ))
        db.send_create_signal('web', ['ProgramParticipant'])

        # Adding model 'SeriesParticipant'
        db.create_table('web_seriesparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Role'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Series'])),
        ))
        db.send_create_signal('web', ['SeriesParticipant'])

        # Adding model 'SourceParticipant'
        db.create_table('web_sourceparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Role'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Source'])),
        ))
        db.send_create_signal('web', ['SourceParticipant'])

        # Adding model 'DigitalFileParticipant'
        db.create_table('web_digitalfileparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Role'])),
            ('digital_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.DigitalFile'])),
        ))
        db.send_create_signal('web', ['DigitalFileParticipant'])

        # Adding unique constraint on 'DigitalFileParticipant', fields ['role', 'digital_file']
        db.create_unique('web_digitalfileparticipant', ['role_id', 'digital_file_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'DigitalFileParticipant', fields ['role', 'digital_file']
        db.delete_unique('web_digitalfileparticipant', ['role_id', 'digital_file_id'])

        # Deleting model 'DigitalFileLocation'
        db.delete_table('web_digitalfilelocation')

        # Deleting model 'DigitalFile'
        db.delete_table('web_digitalfile')

        # Deleting model 'SourceLocation'
        db.delete_table('web_sourcelocation')

        # Deleting model 'SourceFormat'
        db.delete_table('web_sourceformat')

        # Deleting model 'Source'
        db.delete_table('web_source')

        # Deleting model 'Series'
        db.delete_table('web_series')

        # Deleting model 'Rights'
        db.delete_table('web_rights')

        # Deleting model 'Genre'
        db.delete_table('web_genre')

        # Deleting model 'Subject'
        db.delete_table('web_subject')

        # Deleting model 'Person'
        db.delete_table('web_person')

        # Deleting model 'Role'
        db.delete_table('web_role')

        # Deleting model 'Program'
        db.delete_table('web_program')

        # Removing M2M table for field subjects on 'Program'
        db.delete_table('web_program_subjects')

        # Deleting model 'ProgramParticipant'
        db.delete_table('web_programparticipant')

        # Deleting model 'SeriesParticipant'
        db.delete_table('web_seriesparticipant')

        # Deleting model 'SourceParticipant'
        db.delete_table('web_sourceparticipant')

        # Deleting model 'DigitalFileParticipant'
        db.delete_table('web_digitalfileparticipant')


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
            'Meta': {'object_name': 'Genre'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'web.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'first_broadcast': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'member_of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Series']", 'blank': 'True'}),
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
            'Meta': {'object_name': 'Series'},
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
            'Meta': {'object_name': 'Source'},
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.SourceFormat']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.SourceLocation']"}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'recorded_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tracks': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        'web.sourceformat': {
            'Meta': {'object_name': 'SourceFormat'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'web.sourcelocation': {
            'Meta': {'object_name': 'SourceLocation'},
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
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['web']
