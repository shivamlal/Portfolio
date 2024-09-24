from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import  staticfiles_storage
from .forms import ContactForm
from .models import Experience
from .forms import ExperienceForm
from .models import Project
from .models import Resume
# Create your views here.

def about(request):
    return render(request, 'resume/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'resume/projects.html', {'projects': projects})


def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')  # Order by start date, latest first
    return render(request, 'resume/experience.html', {'experiences': experiences})


def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience') # Redirect to the experience list page
    else:
        form = ExperienceForm()
    
    return render(request, 'resume/add_experience.html', {'form': form})


def certificate(request):
    return render (request, "resume/certificate.html")



def resume(request):
    try:
        latest_resume = Resume.objects.latest('uploaded_at')
        resume_path = latest_resume.file.path
        
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    except Resume.DoesNotExist:
        return HttpResponse("Resume not found", status=404)


def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Thanks for connecting !")  # Redirect to a success page or URL
    else:
        fm = ContactForm()
    return render (request,"resume/contact.html",{'form': fm})