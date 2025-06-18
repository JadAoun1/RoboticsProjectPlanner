from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db import connection
import logging

logger = logging.getLogger(__name__)


def test_db(request):
    """Simple view to test database connectivity"""
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        
        # Test user model
        user_count = User.objects.count()
        
        return HttpResponse(f"Database test successful. Users in database: {user_count}")
    except Exception as e:
        logger.error(f"Database test failed: {e}")
        return HttpResponse(f"Database test failed: {e}", status=500)


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        try:
            logger.info("SignUp form is valid, attempting to save user")
            response = super().form_valid(form)
            logger.info(f"User created successfully: {self.object.username}")
            return response
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            form.add_error(None, f"Error creating account: {e}")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        logger.error(f"SignUp form is invalid: {form.errors}")
        return super().form_invalid(form)
