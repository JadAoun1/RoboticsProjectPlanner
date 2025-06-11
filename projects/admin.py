from django.contrib import admin
from .models import Project, ProjectPart, ProjectTool, ProjectNote, MoodboardImage


class ProjectPartInline(admin.TabularInline):
    model = ProjectPart
    extra = 1


class ProjectToolInline(admin.TabularInline):
    model = ProjectTool
    extra = 1


class ProjectNoteInline(admin.TabularInline):
    model = ProjectNote
    extra = 1


class MoodboardImageInline(admin.TabularInline):
    model = MoodboardImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('project_name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProjectPartInline, ProjectToolInline, ProjectNoteInline, MoodboardImageInline]


@admin.register(ProjectPart)
class ProjectPartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'project', 'quantity', 'estimated_cost_per_unit', 'actual_cost_per_unit')
    list_filter = ('project', 'created_at')
    search_fields = ('part_name', 'project__project_name')


@admin.register(ProjectTool)
class ProjectToolAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'project', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('tool_name', 'project__project_name')


@admin.register(ProjectNote)
class ProjectNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_at', 'updated_at')
    list_filter = ('project', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'project__project_name')


@admin.register(MoodboardImage)
class MoodboardImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'image_url', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('caption', 'project__project_name')
