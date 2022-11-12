from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members
from .models import Created

def index(request):
  mymembers = Members.objects.all().values()
  create = Created.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'create': create,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))


# wk 10 proj
def addDay(request):
  template = loader.get_template('addDay.html')
  return HttpResponse(template.render({}, request))

def addrecordDay(request):
  x = request.POST['day']
  member = Created(day=x)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def deleteDay(request, id):
  member = Created.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def updateDay(request, id):
  create = Created.objects.get(id=id)
  template = loader.get_template('updateDay.html')
  context = {
    'create': create,
  }
  return HttpResponse(template.render(context, request))

def updaterecordDay(request, id):
  x = request.POST['d']
  member = Created.objects.get(id=id)
  member.day = x
  member.save()
  return HttpResponseRedirect(reverse('index'))