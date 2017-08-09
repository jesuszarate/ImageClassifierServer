from django import forms
from django.db import models
from django.shortcuts import render, HttpResponse
import json

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
    image = forms.ImageField()


class UploadFileForm(forms.Form):
    file  = forms.FileField()


def handle_uploaded_file(f):
    with open('team/Classifier/images/name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_pic(request):

    #if request.method == 'POST':

    #form = UploadFileForm(request.POST or None, request.FILES or None)
    #if form.is_valid():
    handle_uploaded_file(request.FILES['image'])

    scores = classify("name")

    data = json.dumps(scores)

    return HttpResponse(data)
    #return HttpResponse(data, content_type='application/json')

    #return HttpResponse('upload.html')

#else:
    #form = UploadFileForm()
    #return HttpResponse('upload.html')
