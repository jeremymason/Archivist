from django.db.models import CharField
from django.db.models import DateField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.db.models import ManyToManyField
from django.db.models import TextField

class DigitalFileLocations(Model):
    location = CharField(max_length=500, null=False)

    def __unicode__(self):
        return self.location


class DigitalFile(Model):
    program = ForeignKey('Program', null=True)
    format = CharField(max_length=500)
    sample_rate = IntegerField(null=True)
    size = IntegerField(null=True)
    bit_depth = IntegerField(max_length=500, null=False)
    locations = ForeignKey(DigitalFileLocations, null=True)
    tracks = IntegerField(null=True)
    date_digitized = DateField(null=True)

    def __unicode__(self):
        return self.format + " " + self.sample_rate


class DigitalFileLocation(Model):
    location = CharField(max_length=500, null=False)

    def __unicode__(self):
        return self.location

class SourceFormat(Model):
    name = CharField(max_length=50, null=False)

    def __unicode__(self):
        return self.name


class Source(Model):
    number = IntegerField(null=False)
    format = ForeignKey(SourceFormat, null=True)
    speed = CharField(max_length=500, null=False)
    tracks = IntegerField(null=True)
    recorded_date = DateField(null=True)
    location = CharField(max_length=500, null=True)

    def __unicode__(self):
        return self.number + " " + self.format + " " + self.speed


class Series(Model):
    name = CharField(max_length=500, null=False)
    abbreviation = CharField(max_length=50, null=True)
    description = TextField(null=True)

    def __unicode__(self):
        return self.name + "("+ self.abbreviation + ")"

    class Meta:
        verbose_name_plural = "Series"


class Rights(Model):
    right_type = CharField(max_length=50, null=False)
    right_type_source = CharField(max_length=500, blank=True)
    
    def __unicode__(self):
        return self.right_type

    class Meta:
        verbose_name_plural = "Rights"


class Genre(Model):
    """ A record represents a single genre """
    genre = CharField(max_length=100, null=False)
    source = CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.genre


class Subject(Model):
    """ A record represents a single program subject """
    subject = CharField(max_length=100, null=False)
    source = CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.subject


class Person(Model):
    first_name = CharField(max_length=200, null=False)
    last_name = CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.last_name + ", "+ self.first_name

    class Meta:
        verbose_name_plural = "People"


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
        return self.role



class Program(Model):
    title = CharField(max_length=500, null=False)
    description = TextField(blank=True)
    genre = ForeignKey(Genre)
    subjects = ManyToManyField(Subject)
    duration = CharField(max_length=20, blank=True)
    first_broadcast = CharField(max_length=25, blank=True)
    member_of = ForeignKey(Series, blank=True)
    rights = ForeignKey(Rights, blank=True)
    people = ManyToManyField(Person, through='ProgramParticipant')

    def __unicode__(self):
        return self.title


# ???
# confusion here
# ???
#class Person(Model):
#    first_name = CharField(max_length=200, null=False)
#    last_name = CharField(max_length=200, null=False)
#    role = ForeignKey("Role")
#    content_type = models.ForeignKey(ContentType)
#    object_id = models.PositiveIntegerField()
#    content_object = generic.GenericForeignKey('content_type', 'object_id')
#
#    def __unicode__(self):
#        return self.first_name + " " + self.last_name



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

