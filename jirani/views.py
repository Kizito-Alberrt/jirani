
from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import neighbourhood
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.
def home(request):
    total_activity = neighbourhood.objects.all().count()
    context = {
        
        'total_activity': total_activity,
    }

  

    return render(request, 'home.html',context)

def search(request):
    activity = neighbourhood.objects.all()

    if 'search' in request.GET:
        query = request.GET.get('search')
        queryset = activity.filter(Q(user__icontains='search'))

    if request.GET.get('houses'):
        results = queryset.filter(Q(topic__icontains='houses'))
        topic = 'houses'

    elif request.GET.get('facilities'):
        results = queryset.filter(Q(topic__title__icontains="facilities"))
        topic="facilities"
    elif request.GET.get("schools"):
        results = queryset.filter(Q(topic__title__icontains="schools"))
        topic="schools"
    elif request.GET.get("hospitals"):
        results = queryset.filter(Q(topic__title__icontains="hospitals"))
        topic="hospitals"
    elif request.GET.get("events"):
        results = queryset.filter(Q(topic__title__icontains="events"))
        topic="events"
    elif request.GET.get("neighbours"):
        results = queryset.filter(Q(topic__title__icontains="neighbours"))
        topic="neighbours"
    elif request.GET.get("markets"):
        results = queryset.filter(Q(topic__title__icontains="markets"))
        topic="markets"
    elif request.GET.get("recreation"):
        results = queryset.filter(Q(topic__title__icontains="recreation"))
        topic="recreation"

    total = results.count()

    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "topic":topic,
        "page":page,
        "total":total,
        "query":query,
        "results":results,
    }
    return render(request, "search.html", context)

def detail(request, slug):
    recipe = get_object_or_404(neighbourhood, slug=slug)
    context = {
        "recipe":recipe,
    }
    return render(request, "detail.html", context)

def houses(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'houses.html')

def schools(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'schools.html')

def hospitals(request):
    return render(request, 'hospitals.html')

    
def facilities(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'facilities.html')

def markets(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'markets.html')

def neighbours(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'neighbours.html')

def recreation(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'recreation.html')

def events(request):
    neighbours = neighbourhood.objects.all()
    return render(request, 'events.html')
    
