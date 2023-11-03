from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from .models import Url
from django.urls import reverse

# Create your views here.

def index (request):
    """ index page functionality """

    return render(request, 'urlshortner/index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['url_link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        
        index_url = request.build_absolute_uri(reverse('index'))
        return HttpResponse(index_url+uid)

def go_to_url(request, pk):
    try:
        url_details = Url.objects.get(uuid=pk)
        return redirect(url_details.link)
    except Url.DoesNotExist:
        return redirect('index')     