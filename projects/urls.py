from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Project CRUD
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='delete'),
    
    # Project components (parts, tools, notes, moodboard)
    path('<int:project_id>/parts/add/', views.ProjectPartCreateView.as_view(), name='part_create'),
    path('parts/<int:pk>/edit/', views.ProjectPartUpdateView.as_view(), name='part_update'),
    path('parts/<int:pk>/delete/', views.ProjectPartDeleteView.as_view(), name='part_delete'),
    
    path('<int:project_id>/tools/add/', views.ProjectToolCreateView.as_view(), name='tool_create'),
    path('tools/<int:pk>/edit/', views.ProjectToolUpdateView.as_view(), name='tool_update'),
    path('tools/<int:pk>/delete/', views.ProjectToolDeleteView.as_view(), name='tool_delete'),
    
    path('<int:project_id>/notes/add/', views.ProjectNoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', views.ProjectNoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.ProjectNoteDeleteView.as_view(), name='note_delete'),
    
    path('<int:project_id>/moodboard/add/', views.MoodboardImageCreateView.as_view(), name='moodboard_create'),
    path('moodboard/<int:pk>/edit/', views.MoodboardImageUpdateView.as_view(), name='moodboard_update'),
    path('moodboard/<int:pk>/delete/', views.MoodboardImageDeleteView.as_view(), name='moodboard_delete'),
] 