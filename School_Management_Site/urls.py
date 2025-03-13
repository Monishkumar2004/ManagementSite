# Import necessary modules for URL configuration
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Import views from different modules
from . import views, HOD_views, Staff_views, Student_views

# List of URL patterns
urlpatterns = [
    # URL for the admin interface
    path('admin/', admin.site.urls),

    # URL for the base template
    path('base/', views.base, name="base"),

    # Login-related URLs
    path('', views.login_view, name="login_path"),  # Login page
    path('doLogin/', views.doLogin, name="doLogin"),  # Handle login logic
    path('doLogout/', views.doLogout, name="doLogout_path"),  # Handle logout logic

    # Profile-related URLs
    path('profile/', views.profile, name="profile_path"),  # View user profile
    path('update_profile/', views.update_profile, name="update_profile_path"),  # Update user profile

    # HOD-related URLs
    path('Hod/home/', HOD_views.home, name="hod_home"),  # HOD home page
    path('Hod/add_student/', HOD_views.add_student, name="add_student_path"),  # Add a new student
    path('Hod/view_student/', HOD_views.view_student, name="view_student_path"),  # View all students
    path('Hod/edit_student/<str:id>', HOD_views.edit_student, name="edit_student_path"),  # Edit a student's details
    path('HOD/update_student/', HOD_views.update_student, name="update_student_path"),  # Update a student's details
    path('HOD/delete_student/<str:id>', HOD_views.delete_student, name="delete_student_path"),  # Delete a student
    path('Hod/Grade/Add/', HOD_views.add_course, name="add_grade_path"),  # Add a new course

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve media files (e.g., images) from the MEDIA_ROOT directory
