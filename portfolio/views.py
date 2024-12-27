from django.shortcuts import render
from .models import Skill, Project, Experience, Education, About

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    return render(request, 'portfolio/home.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'education': education,
    })
