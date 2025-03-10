"""
URL configuration for School_Management_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, HOD_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name = "base"),

    # login paths
    path('', views.login_view, name = "login_path"),
    path('doLogin/', views.doLogin, name = "doLogin"),
    path('doLogout/', views.doLogout, name = "doLogout_path"),

    # Profile path
    path('profile/', views.profile, name = "profile_path"),
    path('update_profile/', views.update_profile, name = "update_profile_path"),

    # HOD paths
    path('Hod/home/', HOD_views.home, name = "hod_home"),
    path('Hod/add_student/', HOD_views.add_student, name = "add_student_path" ),
    path('Hod/view_student/', HOD_views.view_student, name = "view_student_path"),
    path('Hod/edit_student/<str:id>', HOD_views.edit_student, name = "edit_student_path"),
    path('HOD/update_student/', HOD_views.update_student, name = "update_student_path"),
    path('HOD/delete_student/<str:id>', HOD_views.delete_student, name = "delete_student_path"),
    


] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
