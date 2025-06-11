from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    """Project model - represents a robotics project"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
        
    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})
    
    def get_total_estimated_cost(self):
        """Calculate total estimated cost from all parts"""
        return sum(part.get_total_cost() for part in self.parts.all())


class ProjectPart(models.Model):
    """Parts/components needed for a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='parts')
    part_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    estimated_cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actual_cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['part_name']
        
    def __str__(self):
        return f"{self.part_name} (x{self.quantity})"
    
    def get_total_cost(self):
        """Get total cost (actual if available, otherwise estimated)"""
        cost_per_unit = self.actual_cost_per_unit or self.estimated_cost_per_unit
        if cost_per_unit:
            return cost_per_unit * self.quantity
        return 0


class ProjectTool(models.Model):
    """Tools needed for a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tools')
    tool_name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['tool_name']
        
    def __str__(self):
        return self.tool_name


class ProjectNote(models.Model):
    """Notes and documentation for a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200, blank=True, default='Note')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
        
    def __str__(self):
        return f"{self.title} - {self.project.project_name}"


class MoodboardImage(models.Model):
    """Images and inspiration for project moodboard"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='moodboard_images')
    image_url = models.URLField()
    caption = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Moodboard image for {self.project.project_name}"
