from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import ForeignKey
from django.db.models import FloatField
from django.db.models import IntegerField
from django.db.models import Model
from django.db.models import ManyToManyField
from django.db.models import OneToOneField
from django.db.models import TextField


class DigitalFileLocation(Model):
    digital_file = ForeignKey('DigitalFile')
    location = CharField(max_length=500, blank=False)

    def __unicode__(self):
        return self.location

    def natural_key(self):
        return((self.location),)


class DigitalFile(Model):
    program = OneToOneField('Program')
    format = CharField(max_length=50, blank=True)
    sample_rate = IntegerField(blank=True)
    size = FloatField(blank=True)
    bit_depth = IntegerField(blank=True)
    tracks = IntegerField(blank=True)
    date_digitized = DateField(blank=True)
    who_digitized = ManyToManyField('Person', through='DigitalFileParticipant')

    def __unicode__(self):
        return str(self.program.title) + " (format: " + str(self.format) + ", rate: " + str(self.sample_rate) + ")"

    def natural_key(self):
        return((str(str(self.program.title) + " (format: " + str(self.format) + ", rate: " + str(self.sample_rate) + ")"),))


class SourceLocation(Model):
    location = CharField(max_length=500, null=False)

    def __unicode__(self):
        return self.location

    def natural_key(self):
        return((self.location,))

    class Meta:
        ordering= ['location']


class SourceFormat(Model):
    name = CharField(max_length=50, null=False)

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return((self.name,))

    class Meta:
        ordering= ['name']


class Source(Model):
    name = CharField(max_length=100, blank=False)
    location = ForeignKey(SourceLocation, blank=False)
    format = ForeignKey(SourceFormat, blank=False, null=False)
    speed = CharField(max_length=500, blank=True)
    tracks = IntegerField(blank=True, null=True)
    recorded_date = DateField(blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def natural_key(self):
        return((self.name,))

    class Meta:
        ordering= ['name']


class Series(Model):
    name = CharField(max_length=500, null=False)
    abbreviation = CharField(max_length=50, null=True)
    description = TextField(null=True)

    def __unicode__(self):
        return self.name + "("+ self.abbreviation + ")"

    def natural_key(self):
        return((self.name,))

    class Meta:
        verbose_name_plural = "Series"
        ordering= ['name']


class Rights(Model):
    right_type = CharField(max_length=50, null=False)
    right_type_source = CharField(max_length=500, blank=True)
    
    def __unicode__(self):
        return self.right_type

    def natural_key(self):
        return((self.right_type,))

    class Meta:
        verbose_name_plural = "Rights"


class Genre(Model):
    """ A record represents a single genre """
    genre = CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.genre

    def natural_key(self):
        return((self.genre,))

    class Meta:
        ordering= ['genre']


class Subject(Model):
    """ A record represents a single program subject """
    subject = CharField(max_length=250, blank=False)

    def __unicode__(self):
        return self.subject

    def natural_key(self):
        return((self.subject,))

    class Meta:
        ordering= ['subject']


class Person(Model):
    first_name = CharField(max_length=200, null=False)
    last_name = CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.last_name + ", "+ self.first_name

    def natural_key(self):
        return((str(self.first_name+" "+self.last_name),))

    class Meta:
        verbose_name_plural = "People"
        ordering = ['last_name', 'first_name']


class Role(Model):
    APPLIES_TO_CHOICES = (
        ('Program', 'Program'),
        ('Series', 'Series'),
        ('Source', 'Source'),
        ('DigitalFile', 'Digital File'),
    )
    role = CharField(max_length=50, null=False)
    applies_to = CharField(max_length=50, null=False, choices=APPLIES_TO_CHOICES)
    source = CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.applies_to + " " + self.role

    def natural_key(self):
        return((self.role,))



class Program(Model):
    ident = CharField(max_length=50, blank=False)
    title = CharField(max_length=500, blank=False)
    description = TextField(blank=True)
    genres = ManyToManyField(Genre)
    subjects = ManyToManyField(Subject)
    source = ForeignKey(Source)
    duration = CharField(max_length=10, blank=True)
    digitized = BooleanField()
    first_broadcast = CharField(max_length=25, blank=True)
    member_of = ForeignKey(Series, blank=True, null=True)
    rights = ForeignKey(Rights, blank=True)
    people = ManyToManyField(Person, through='ProgramParticipant')

    def __unicode__(self):
        return self.title

    def natural_key(self):
        return((self.ident,))

    def program_subjects(self):
        return ", ".join([x.subject for x in self.subjects.all()])

    def program_genres(self):
        return ", ".join([x.genre for x in self.genres.all()])

    class Meta:
        ordering= ['title']


class ProgramParticipant(Model):
    person = ForeignKey(Person)
    role = ForeignKey(Role, limit_choices_to = {'applies_to__exact': 'Program'})
    program = ForeignKey(Program)


class SeriesParticipant(Model):
    person = ForeignKey(Person)
    role = ForeignKey(Role, limit_choices_to = {'applies_to__exact': 'Series'})
    series = ForeignKey(Series)


class SourceParticipant(Model):
    person = ForeignKey(Person)
    role = ForeignKey(Role, limit_choices_to = {'applies_to__exact': 'Source'})
    source = ForeignKey(Source)


class DigitalFileParticipant(Model):
    person = ForeignKey(Person)
    role = ForeignKey(Role, limit_choices_to = {'applies_to__exact': 'DigitalFile'})
    digital_file = ForeignKey(DigitalFile)

    class Meta:
        unique_together = ("role", "digital_file")

