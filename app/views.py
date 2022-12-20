from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse("successfully inserted the topic record")
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        u=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=n,url=u)[0]
        w.save()
        return HttpResponse("successfully inserted the Webpage record")
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    topic=Topic.objects.all()
    webpage=Webpage.objects.all()
    D={'webpage':webpage,'topic':topic}
    if request.method=='POST':
        t=request.POST['topic']
        n=request.POST['name']
        d=request.POST['date']
        tn=Topic.objects.get_or_create(topic_name=t)
        tn.save()
        w=Webpage.objects.get(topic_name=tn,name=n)
        w.save()
        ar=AccessRecords.objects.get_or_create(name=w,date=d)[0]
        ar.save()
    return render(request,'insert_accessrecords.html',D)

def display_selected(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        webpages=Webpage.objects.none()
        print(tn)
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        co={'webpages':webpages}
        return render(request,'show.html',co)
    return render(request,'display_selected.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'checkbox.html',d)