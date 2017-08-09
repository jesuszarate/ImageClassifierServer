from django import forms
from django.db import models
#from django.forms import models
from django.shortcuts import render, HttpResponse
import json

# from mysite.personal import models
# from django.http import JsonResponse

# Create your views here.
#from mysite.team.ImageUploadForm import ImageUploadForm
#from mysite.team.ExampleModel import ExampleModel
#from mysite.team.ImageUploadForm import UploadFileForm

import sys
print('*'*50)
#print(sys.path.append('..'))
print('*'*50)
#sys.path.append('../Classify)
from .Classifier.classify_image import classify


def team(request):
    return render(request, 'team/team.html')

def about(request):
    return render(request, 'about/about.html')

def chuy(request):
    return render(request, 'members/chuy/profile.html')

def greg(request):
    return render(request, 'members/greg/profile.html')

def yu(request):
    return render(request, 'members/yu/profile.html')

def lance(request):
    return render(request, 'members/lance/profile.html')

def uploadPicture(request):
    return render(request, 'upload_picture.html')

def jj(request):
    d = {}
    d['jj'] = 'arteaga'
    data = json.dumps(d)
    return HttpResponse(data, content_type='application/json')


class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file  = forms.FileField()


def handle_uploaded_file(f):
    with open('Classifier/images/name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_pic(request):

    print("*"*25 + request.method + "*"*25)
    if request.method == 'POST':

        #form = UploadFileForm(request.POST or None, request.FILES or None)
        #if form.is_valid():
        handle_uploaded_file(request.FILES['image'])
        print("*"*25 + "HERE1" + "*"*25)
        scores = classify("name")
        print("*"*25 + "HERE2" + "*"*25)
        print(scores)
        data = json.dumps(scores)
        print("*"*25 + "HERE3" + "*"*25)
        return HttpResponse(data)
        #return HttpResponse(data, content_type='application/json')

        #return HttpResponse('upload.html')
    else:
        #form = UploadFileForm()
        return HttpResponse('upload.html')
