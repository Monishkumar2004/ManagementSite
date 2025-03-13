from django.shortcuts import redirect, render  # Import necessary modules from Django
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from app.models import Grade, Session_Year, CustomUser ,Student
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
    grade = Grade.objects.all()
    sessions = Session_Year.objects.all()

    if request.method == "POST":
        student_image = request.FILES.get("student_image")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        grade = request.POST.get("grade")
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

            grade = Grade.objects.get(id = grade)

            student = Student(
                admin = user,
                gender = gender,
                date_of_birth = date_of_birth,
                grade_id = grade,
                # joining_date = joining_date,
                mobile_number = mobile_number,
                # admission_number = admission_number,
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
        'grade': grade,
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
    grade = Grade.objects.all()
    context = {
        'student' : student,
        'grade' : grade,
    }

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        print(profile_pic)

    return render(request, 'HOD/edit_student.html', context)


def update_student(request):

    grade = Grade.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
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

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
                user.set_password(password)

        if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic

        user.save()

        grade_instance = Grade.objects.get(id = grade_id)

        student = Student.objects.get(admin = student_id)
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.grade_id = grade_instance 
                # joining_date = joining_date,
        student.mobile_number = mobile_number
        # student.admission_number = admission_number  feature changed to automatically add admission number
        student.section = section
        student.father_name = father_name
        student.father_occupation = father_occupation
        student.father_mobile =father_mobile
        student.father_email = father_email
        student.mother_name = mother_name
        student.mother_occupation = mother_occupation
        student.mother_mobile = mother_mobile
        student.mother_email = mother_email
        student.present_address = present_address
        student.permanent_address = permanent_address

        student.save()
        messages.success(request, "Record is updated Successfully.")
        return redirect("view_student_path")
    

        

    return render(request, 'HOD/edit_student.html')


def delete_student(request, id):
     student = CustomUser.objects.get(id = id)
     student.delete()
     messages.success(request, "Student deleted Successfully.")
     return redirect("view_student_path")


def add_course(request):
     
    return render(request, 'HOD/add_class.html')