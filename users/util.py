from .models import Skill,profile
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def paginatePages(request,profile,result):

    page=request.GET.get('page')
    paginator=Paginator(profile,result)
    try:
        profile=paginator.page(page)
    except EmptyPage:
        page=paginator.page_range
        profile=paginator.page(page)
    except PageNotAnInteger:
        page=1
        profile=paginator.page(page)

    leftIndex=(int(page) - 4)
    if leftIndex<1:
        leftIndex=1
    rightIndex=(int(page) + 5)
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custom_range = range(leftIndex,rightIndex)
    return custom_range , profile

def searchProfile(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    skill=Skill.objects.filter(name__icontains=search_query)
    profiles=profile.objects.distinct().filter(
        Q(first_name__icontains=search_query) | 
        Q(short_bio__icontains=search_query)|
        Q(skill__in=skill))
    return profiles , search_query