from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_list(request):
    projects = Project.objects.all()   # in this model get me all objects 
    return render(request, 'projects/projects_list.html', {'projects': projects})

def experience_list(request):
    return render(request, 'experiences/experience_list.html')