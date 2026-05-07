import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Project, Skill, ContactMessage
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(is_featured=True)
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


class SkillsView(TemplateView):
    template_name = 'skills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group skills by category while preserving Meta ordering (category, name)
        grouped = {}
        for skill in Skill.objects.all():
            grouped.setdefault(skill.category, []).append(skill)
        context['skills_by_category'] = grouped
        return context


class ResumeView(TemplateView):
    template_name = 'resume.html'


class ResumePDFView(View):
    def get(self, request):
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'resume.pdf')
        if not os.path.exists(pdf_path):
            raise Http404
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        return response


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        ContactMessage.objects.create(**form.cleaned_data)
        messages.success(
            self.request,
            "Thanks for reaching out! I'll get back to you soon.",
        )
        return super().form_valid(form)
