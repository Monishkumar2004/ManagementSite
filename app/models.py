# Import necessary modules from Django for database models and custom user authentication
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model that extends the built-in AbstractUser
class CustomUser(AbstractUser):
    # Email field with unique constraint and maximum length
    email = models.EmailField(unique=True, max_length=70)  # Ensures each user has a unique email address

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


# Model representing a subject (e.g., Mathematics, History)
class Subject(models.Model):
    name  = models.CharField(max_length=100)  # Name of the subject

    # Returns the name of the subject as a string representation
    def __str__(self):
        return self.name


# Model representing a grade or course offered in the school
class Grade(models.Model):
    """
    Represents a course offered in the school.

    Attributes:
        name (CharField): The name of the course (e.g., "Mathematics", "History").  Max length of 100 characters.
        created_at (DateTimeField):  The date and time when the course was created.  Automatically set when the object is first created.
        updated_at (DateTimeField): The date and time when the course was last updated. Automatically updated whenever the object is saved.

    Methods:
        __str__():  Returns the name of the course as a string representation of the object.  This is useful for displaying the course in the admin panel and other places.
    """
    name = models.CharField(max_length=100)  # Name of the grade
    subjects = models.ManyToManyField(Subject, related_name="grades")  # Many-to-many relationship with subjects
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the grade was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the grade was last updated

    # Returns the name of the grade as a string representation
    def __str__(self):
        return self.name


# Model representing an academic session year (e.g., 2023-2024)
class Session_Year(models.Model):
    """
    Represents an academic session year (e.g., 2023-2024).

    Attributes:
        session_start (CharField): The starting year of the session.  Max length of 100 characters.
        session_end (CharField): The ending year of the session. Max length of 100 characters.
    """
    session_start = models.CharField(max_length = 100)  # Starting year of the session
    session_end = models.CharField(max_length = 100)  # Ending year of the session

    # Returns the session year as a string representation (e.g., "2023 to 2024")
    def __str__(self):
        return self.session_start + " to " + self.session_end


# Function to generate a unique admission number for each student
def generate_admission_number():
    # Fetch the latest student based on ID (newest student)
    last_student = Student.objects.order_by('-id').first() 

    # If there are existing students, increment the admission number
    if last_student:
        # Extract the numeric part of the admission number and increment it
        last_number = int(last_student.admission_number.split('-')[-1])
        new_number = last_number + 1
    else:
        # If no students exist, start with admission number 1
        new_number = 1
    
    # Format the admission number as "ADM-XXXX"
    return f"ADM-{str(new_number).zfill(4)}"


# Model representing a student in the school
class Student(models.Model):
    """
    Represents a student in the school.

    Methods:
        __str__(): Returns the student's full name as a string representation.
    """
    
    # One-to-one relationship with the CustomUser model
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # Student's gender
    gender = models.CharField(max_length=100)

    # Student's date of birth
    date_of_birth = models.DateField(null=True, blank=True)  

    # Foreign key referencing the Grade model
    grade_id = models.ForeignKey('Grade', on_delete=models.DO_NOTHING)
    
    # Timestamp when the student was added
    joined_at = models.DateTimeField(auto_now_add=True)
    
    # Student's mobile number
    mobile_number = models.CharField(max_length=15, blank=True, null=True)  

    # Unique admission number generated automatically
    admission_number = models.CharField(max_length=50, unique=True, editable=False, default=generate_admission_number)  

    # Student's section (e.g., A, B, C)
    section = models.CharField(max_length=20, blank=True, null=True)

    # Father's name
    father_name = models.CharField(max_length=100, blank=True, null=True)

    # Mother's name
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Father's occupation
    father_occupation = models.CharField(max_length=100, blank=True, null=True)

    # Mother's occupation
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    
    # Father's mobile number
    father_mobile = models.CharField(max_length=15, blank=True, null=True)  

    # Mother's mobile number
    mother_mobile = models.CharField(max_length=15, blank=True, null=True)  

    # Father's email
    father_email = models.EmailField(max_length=100, blank=True, null=True)  

    # Mother's email
    mother_email = models.EmailField(max_length=100, blank=True, null=True)  

    # Present address
    present_address = models.TextField(blank=True, null=True)

    # Permanent address
    permanent_address = models.TextField(blank=True, null=True)
    
    # Foreign key referencing the Session_Year model
    Session_Year_id = models.ForeignKey('Session_Year', on_delete=models.DO_NOTHING, blank=True, null=True)
    
    # Timestamp when the student's details were last updated
    updated_at = models.DateTimeField(auto_now=True)

    # Returns the student's full name as a string representation
    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

    # Meta class to set verbose names for the model
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
