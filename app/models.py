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
    profile_pic = models.ImageField(upload_to="profile_pics")  # Uploads profile pictures to specified directory
