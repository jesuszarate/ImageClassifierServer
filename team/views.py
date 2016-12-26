from django.shortcuts import render

# Create your views here.
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