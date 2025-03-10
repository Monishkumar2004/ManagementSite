from django.shortcuts import redirect, render  # Import necessary modules from Django
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from app.models import Course, Session_Year, CustomUser ,Student
from django.contrib import messages
# Apply the login_required decorator.
# This ensures that only authenticated users can access this view.
# If a user is not logged in, they will be redirected to the URL specified by 'login_url'.
@login_required(login_url='/')
def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'HOD/home.html' template.
    """
    # Render the 'HOD/home.html' template and return the HTTP response.
    # The 'render' function combines the template with the context (in this case, an empty context)
    # to produce the final HTML output.
    return render(request, 'HOD/home.html')

@login_required(login_url = '/')
def add_student(request):
    '''
    Function to add students only accessible to the HOD
    '''
    courses = Course.objects.all()
    sessions = Session_Year.objects.all()

    if request.method == "POST":
        student_image = request.FILES.get("student_image")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        course_id = request.POST.get("course")
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get('password')
        # joining_date = request.POST.get("joining_date")
        mobile_number = request.POST.get("mobile_number")
        admission_number = request.POST.get("admission_number")
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

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email already registered !")
            return redirect("add_student_path")
            
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username already taken !")
            return redirect("add_student_path")
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = student_image,
                user_type = 3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)

            student = Student(
                admin = user,
                gender = gender,
                date_of_birth = date_of_birth,
                course_id = course,
                # joining_date = joining_date,
                mobile_number = mobile_number,
                admission_number = admission_number,
                section = section,
                father_name = father_name,
                father_occupation = father_occupation,
                father_mobile =father_mobile,
                father_email = father_email,
                mother_name = mother_name,
                mother_occupation = mother_occupation,
                mother_mobile = mother_mobile,
                mother_email = mother_email,
                present_address = present_address,
                permanent_address = permanent_address,

            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + " is added successfully." )
            return redirect("add_student_path")


    context = {
        'courses': courses,
        'sessions': sessions,
    }



    return render(request, 'HOD/add_student.html', context)

def view_student(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'HOD/view_student.html', context)

def edit_student(request, id):
    student = Student.objects.get(id = id)
    course = Course.objects.all()
    context = {
        'student' : student,
        'course' : course,
    }

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        print(profile_pic)

    return render(request, 'HOD/edit_student.html', context)