# Import necessary modules from Django
from django.shortcuts import redirect, render  
from django.contrib.auth.decorators import login_required  
from app.models import Grade, Session_Year, CustomUser, Student
from django.contrib import messages

# Apply the login_required decorator to ensure only authenticated users can access this view
@login_required(login_url='/')
def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'HOD/home.html' template.
    """
    # Render the 'HOD/home.html' template and return the HTTP response
    return render(request, 'HOD/home.html')


@login_required(login_url='/')  # Ensure only logged-in users can access this view
def add_student(request):
    '''
    Function to add students only accessible to the HOD
    '''
    # Fetch all grades and session years
    grade = Grade.objects.all()
    sessions = Session_Year.objects.all()

    if request.method == "POST":  # Check if the request method is POST
        # Get the student's image from the request
        student_image = request.FILES.get("student_image")
        
        # Get other student details from the request
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        grade_id = request.POST.get("grade")
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get('password')
        # joining_date = request.POST.get("joining_date")
        mobile_number = request.POST.get("mobile_number")
        # admission_number = request.POST.get("admission_number")
        section = request.POST.get("section")
        father_name = request.POST.get("father_name")
        father_occupation = request.POST.get("father_occupation")
        father_mobile = request.POST.get("father_mobile")
        father_email = request.POST.get("father_email")
        mother_name = request.POST.get("mother_name")
        mother_occupation = request.POST.get("mother_occupation")
        mother_mobile = request.POST.get("mother_mobile")
        mother_email = request.POST.get("mother_email")
        present_address = request.POST.get("present_address")
        permanent_address = request.POST.get("permanent_address")

        # Check if the email is already registered
        if CustomUser.objects.filter(email=email).exists():
            # Display warning if email is already in use
            messages.warning(request, "Email already registered !")
            return redirect("add_student_path")
            
        # Check if the username is already taken
        if CustomUser.objects.filter(username=username).exists():
            # Display warning if username is already taken
            messages.warning(request, "Username already taken !")
            return redirect("add_student_path")
        else:
            # Create a new CustomUser instance
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=student_image,
                user_type=3,  # Set user type to Student
            )
            # Set the user's password
            user.set_password(password)
            # Save the user
            user.save()

            # Get the selected grade instance
            grade_instance = Grade.objects.get(id=grade_id)

            # Create a new Student instance
            student = Student(
                admin=user,  # Link the student to the user
                gender=gender,
                date_of_birth=date_of_birth,
                grade_id=grade_instance,
                # joining_date=joining_date,
                mobile_number=mobile_number,
                # admission_number=admission_number,
                section=section,
                father_name=father_name,
                father_occupation=father_occupation,
                father_mobile=father_mobile,
                father_email=father_email,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                mother_mobile=mother_mobile,
                mother_email=mother_email,
                present_address=present_address,
                permanent_address=permanent_address,

            )
            # Save the student
            student.save()
            # Display success message
            messages.success(request, user.first_name + " " + user.last_name + " is added successfully.")
            return redirect("add_student_path")

    # Create a context dictionary with grades and sessions
    context = {
        'grade': grade,
        'sessions': sessions,
    }

    # Render the 'HOD/add_student.html' template with the context
    return render(request, 'HOD/add_student.html', context)


def view_student(request):
    # Fetch all students
    student = Student.objects.all()
    # Create a context dictionary with students
    context = {
        'student': student
    }
    # Render the 'HOD/view_student.html' template with the context
    return render(request, 'HOD/view_student.html', context)


def edit_student(request, id):
    # Get the student to edit by ID
    student = Student.objects.get(id=id)
    # Fetch all grades
    grade = Grade.objects.all()
    # Create a context dictionary with the student and grades
    context = {
        'student': student,
        'grade': grade,
    }

    if request.method == "POST":  # Check if the request method is POST
        # Get the new profile picture from the request
        profile_pic = request.FILES.get('profile_pic')
        print(profile_pic)

    # Render the 'HOD/edit_student.html' template with the context
    return render(request, 'HOD/edit_student.html', context)


def update_student(request):
    # Fetch all grades
    grade = Grade.objects.all()

    if request.method == "POST":  # Check if the request method is POST
        # Get the student ID from the request
        student_id = request.POST.get("student_id")
        
        # Get other updated fields from the request
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        grade_id = request.POST.get("grade")
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get('password')
        # joining_date = request.POST.get("joining_date")
        mobile_number = request.POST.get("mobile_number")
        # admission_number = request.POST.get("admission_number")
        section = request.POST.get("section")
        father_name = request.POST.get("father_name")
        father_occupation = request.POST.get("father_occupation")
        father_mobile = request.POST.get("father_mobile")
        father_email = request.POST.get("father_email")
        mother_name = request.POST.get("mother_name")
        mother_occupation = request.POST.get("mother_occupation")
        mother_mobile = request.POST.get("mother_mobile")
        mother_email = request.POST.get("mother_email")
        present_address = request.POST.get("present_address")
        permanent_address = request.POST.get("permanent_address")

        # Get the user associated with the student
        user = CustomUser.objects.get(id=student_id)
        
        # Update user fields
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        # Update password if provided
        if password != None and password != "":
            user.set_password(password)

        # Update profile picture if provided
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        # Save the changes
        user.save()

        # Get the selected grade instance
        grade_instance = Grade.objects.get(id=grade_id)

        # Get the student associated with the user
        student = Student.objects.get(admin=student_id)
        
        # Update student fields
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.grade_id = grade_instance 
        # joining_date = joining_date,
        student.mobile_number = mobile_number
        # student.admission_number = admission_number  feature changed to automatically add admission number
        student.section = section
        student.father_name = father_name
        student.father_occupation = father_occupation
        student.father_mobile = father_mobile
        student.father_email = father_email
        student.mother_name = mother_name
        student.mother_occupation = mother_occupation
        student.mother_mobile = mother_mobile
        student.mother_email = mother_email
        student.present_address = present_address
        student.permanent_address = permanent_address

        # Save the changes
        student.save()
        # Display success message
        messages.success(request, "Record is updated Successfully.")
        return redirect("view_student_path")
    

    # Render the 'HOD/edit_student.html' template
    return render(request, 'HOD/edit_student.html')


def delete_student(request, id):
    # Get the user associated with the student to delete
    student = CustomUser.objects.get(id=id)
    # Delete the user (and associated student)
    student.delete()
    # Display success message
    messages.success(request, "Student deleted Successfully.")
    return redirect("view_student_path")


def add_course(request):
    # Render the 'HOD/add_class.html' template
    return render(request, 'HOD/add_class.html')
