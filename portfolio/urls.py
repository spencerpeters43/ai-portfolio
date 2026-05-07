from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('resume/pdf/', views.ResumePDFView.as_view(), name='resume_pdf'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
