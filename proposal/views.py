from django.shortcuts import render
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


def search(request):
    proposals = Proposal.objects.order_by('-date_added')
    if 'topic' in request.GET:
        topic = request.GET['topic']
        if topic:
            pickups = Proposal.objects.filter(topic__icontains=topic)
    context={'proposals':proposals,'pickups':pickups}
    return render(request,'search.html',context)


def topics(request):
    posts=Proposal.objects.order_by('-date_added')
    #pagination
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context={'posts':users}
    return render(request,'topics.html',context)

def detail(request,slug):
    post=Proposal.objects.get(slug=slug)
     # hitcount
    post.project_topic_views=post.project_topic_views+1
    post.save()
    context={'post':post}
    return render(request,'detail.html',context)


def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')