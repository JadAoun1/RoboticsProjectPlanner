from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Project, ProjectPart, ProjectTool, ProjectNote, MoodboardImage


# Dashboard and Project Views
class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/dashboard.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name']
    template_name = 'projects/project_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['project_name']
    template_name = 'projects/project_form.html'
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:dashboard')
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


# Project Parts Views
class ProjectPartCreateView(LoginRequiredMixin, CreateView):
    model = ProjectPart
    fields = ['part_name', 'quantity', 'estimated_cost_per_unit', 'notes']
    template_name = 'projects/part_form.html'
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        form.instance.project = project
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        return context
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.kwargs['project_id']})


class ProjectPartUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectPart
    fields = ['part_name', 'quantity', 'estimated_cost_per_unit', 'actual_cost_per_unit', 'notes']
    template_name = 'projects/part_form.html'
    
    def get_queryset(self):
        return ProjectPart.objects.filter(project__user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


class ProjectPartDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectPart
    template_name = 'projects/part_confirm_delete.html'
    
    def get_queryset(self):
        return ProjectPart.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


# Project Tools Views  
class ProjectToolCreateView(LoginRequiredMixin, CreateView):
    model = ProjectTool
    fields = ['tool_name', 'notes']
    template_name = 'projects/tool_form.html'
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        form.instance.project = project
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        return context
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.kwargs['project_id']})


class ProjectToolUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectTool
    fields = ['tool_name', 'notes']
    template_name = 'projects/tool_form.html'
    
    def get_queryset(self):
        return ProjectTool.objects.filter(project__user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


class ProjectToolDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectTool
    template_name = 'projects/tool_confirm_delete.html'
    
    def get_queryset(self):
        return ProjectTool.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


# Project Notes Views
class ProjectNoteCreateView(LoginRequiredMixin, CreateView):
    model = ProjectNote
    fields = ['title', 'content']
    template_name = 'projects/note_form.html'
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        form.instance.project = project
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.kwargs['project_id']})


class ProjectNoteUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectNote
    fields = ['title', 'content']
    template_name = 'projects/note_form.html'
    
    def get_queryset(self):
        return ProjectNote.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


class ProjectNoteDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectNote
    template_name = 'projects/note_confirm_delete.html'
    
    def get_queryset(self):
        return ProjectNote.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


# Moodboard Views
class MoodboardImageCreateView(LoginRequiredMixin, CreateView):
    model = MoodboardImage
    fields = ['image_url', 'caption']
    template_name = 'projects/moodboard_form.html'
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        form.instance.project = project
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.kwargs['project_id']})


class MoodboardImageUpdateView(LoginRequiredMixin, UpdateView):
    model = MoodboardImage
    fields = ['image_url', 'caption']
    template_name = 'projects/moodboard_form.html'
    
    def get_queryset(self):
        return MoodboardImage.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})


class MoodboardImageDeleteView(LoginRequiredMixin, DeleteView):
    model = MoodboardImage
    template_name = 'projects/moodboard_confirm_delete.html'
    
    def get_queryset(self):
        return MoodboardImage.objects.filter(project__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'pk': self.object.project.pk})
