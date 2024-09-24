from django.urls import path,include
from resume import views

urlpatterns = [
    path('about/',views.about, name="about"),
    path('projects/',views.projects, name="projects"),
    path('experience/',views.experience, name="experience"),
    path('experiences/add/', views.add_experience, name='add_experience'),
    path('certificate/',views.certificate, name="certificate"),
    path('resume/',views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]