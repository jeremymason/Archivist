from django.template import RequestContext, loader
from web.models import Program, Genre, Subject
from django.http import HttpResponse

def index(request):
    t = loader.get_template('home.html')
    programs = Program.objects.all()
    c = RequestContext(request, {
        'programs': programs,
        })
    return HttpResponse(t.render(c))


def genres(request):
    t = loader.get_template('display.html')
    items = Genre.objects.all()
    items = [x.genre for x in items]
    c = RequestContext(request, {
        'item_name': "Genres",
        'items': items,
        })
    return HttpResponse(t.render(c))


def subjects(request):
    t = loader.get_template('display.html')
    items = Subject.objects.all()
    items = [x.subject for x in items]
    c = RequestContext(request, {
        'item_name': "Subjects",
        'items': items,
        })
    return HttpResponse(t.render(c))


def programs(request):
    t = loader.get_template('programs.html')
    programs = Program.objects.all()
    c = RequestContext(request, {
        'programs': programs,
        })
    return HttpResponse(t.render(c))


def program(request, program_id):
    t = loader.get_template('program.html')
    program = Program.objects.get(id__exact=program_id)
    c = RequestContext(request, {
        'program': program,
        })
    return HttpResponse(t.render(c))

