import json
import urllib.error
import urllib.parse
import urllib.request


from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Job


def is_valid_queryparam(param):
    return param != '' and param is not None

def home(request):
    job = Job.objects.all()
    display_all = True
    types = []
    for job_item in job:
        if job_item.type not in types:
            types.append(job_item.type)

    location = request.GET.get('location')
    title = request.GET.get('title')
    job_type = request.GET.get('job_type')

    if is_valid_queryparam(location):
        job = job.filter(location__icontains=location)
        display_all = False

    if is_valid_queryparam(title):
        job = job.filter(title__icontains=title)
        display_all = False

    if is_valid_queryparam(job_type):
        job = job.filter(type=job_type)
        display_all = False


    if is_valid_queryparam(request.GET.get('all')):
        display_all = False
    else:
        job = job[0:10]

    print(len(job))
    return render(request, 'job_list.html', {'page_obj': job, 'types': types, 'display_all': display_all})
