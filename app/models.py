from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model that extends the built-in AbstractUser
class CustomUser(AbstractUser):
    # Email field with unique constraint and maximum length
    email = models.EmailField(unique=True, max_length=70)

    # Specify the field to be used for authentication (overrides default username)
    USERNAME_FIELD = 'email'  # This is the field Django uses for authentication purposes, hence set to "email"

    # Additional fields required for creating a superuser
    REQUIRED_FIELDS = ['username']  # Specify other fields required when creating a superuser

    # Choices for user types
    USER = (
        (1, "HOD"),      # Head of Department
        (2, "Staff"),    # Staff member
        (3, "Student"),  # Student
    )

    # Field to store user type with choices defined above
    user_type = models.CharField(choices=USER, max_length=50, default=1)  # Default user type is HOD

    # Field to store profile picture of the user
    profile_pic = models.ImageField(upload_to="profile_pics", default="assets\img\default.jpg")  # Uploads profile pictures to specified directory

class Course(models.Model):
    """
    Represents a course offered in the school.

    Attributes:
        name (CharField): The name of the course (e.g., "Mathematics", "History").  Max length of 100 characters.
        created_at (DateTimeField):  The date and time when the course was created.  Automatically set when the object is first created.
        updated_at (DateTimeField): The date and time when the course was last updated. Automatically updated whenever the object is saved.

    Methods:
        __str__():  Returns the name of the course as a string representation of the object.  This is useful for displaying the course in the admin panel and other places.
    """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    """
    Represents an academic session year (e.g., 2023-2024).

    Attributes:
        session_start (CharField): The starting year of the session.  Max length of 100 characters.
        session_end (CharField): The ending year of the session. Max length of 100 characters.
    """
    session_start = models.CharField(max_length = 100)
    session_end = models.CharField(max_length = 100)

    def __str__(self):
        return self.session_start + " to " + self.session_end

class Student(models.Model):
    """
    Represents a student in the school.

    Methods:
        __str__(): Returns the student's full name as a string representation.
    """
    
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  # Changed to DateField for better date handling
    course_id = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    
    joined_at = models.DateTimeField(auto_now_add=True)
    
    mobile_number = models.CharField(max_length=15, blank=True, null=True)  # Allowing for formatting
    admission_number = models.CharField(max_length=50, unique=True, null=True, blank=True, default='TEMP')  # Admission numbers may not be strictly numeric
    section = models.CharField(max_length=20, blank=True, null=True)
    
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    
    father_mobile = models.CharField(max_length=15, blank=True, null=True)  # Allowing for formatting
    mother_mobile = models.CharField(max_length=15, blank=True, null=True)  # Allowing for formatting
    
    father_email = models.EmailField(max_length=100, blank=True, null=True)  # Changed to EmailField
    mother_email = models.EmailField(max_length=100, blank=True, null=True)  # Changed to EmailField
    
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    
    Session_Year_id = models.ForeignKey('Session_Year', on_delete=models.DO_NOTHING, blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"