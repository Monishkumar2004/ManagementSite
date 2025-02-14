from django.shortcuts import render, redirect, HttpResponse  # Import necessary functions for rendering and redirecting
from app.EmailBackend import EmailBackend  # Import the custom EmailBackend for authentication
from django.contrib.auth import authenticate, login, logout  # Import authentication functions
from django.contrib import messages
from django.contrib.auth.decorators import login_required #Import login required module for restricting access to secret pages 
from app.models import CustomUser

def base(request):
    """
    Render the base template.
    """
    return render(request, "base.html")  # Render the base.html template

def login_view(request):
    """
    Render the login page.
    """
    return render(request, "login.html")  # Render the login.html template

def doLogin(request):
    """
    Handle user login logic.
    """
    if request.method == "POST":  # Check if the request method is POST
        # Authenticate user using email and password
        # user = EmailBackend.authenticate(   
        user = authenticate(
            request,
            username=request.POST.get("email"),  # Get email from POST data
            password=request.POST.get("password"),  # Get password from POST data
        )

        if user is not None:  # Check if authentication was successful
            login(request, user)  # Log in the user
            
            user_type = user.user_type  # Get the user's type
            
            # Redirect based on user type
            if user_type == '1':  # If user is HOD
                return redirect('hod_home')
            elif user_type == '2':  # If user is Staff
                return HttpResponse("This is staff panel")
            elif user_type == '3':  # If user is Student
                return HttpResponse("This is student panel")
            else:
                # Message
                messages.error(request, "Email and Password Invalid !")
                return redirect('login_path')  # Redirect to login if user type is unrecognized
        
        else:
            # Message
            messages.error(request, "Email and Password Invalid !")
            return redirect('login_path')  # Redirect to login if authentication failed
        

def doLogout(request):
    logout(request)
    return redirect('login_path')



# Profile Views
@login_required(login_url="/")
def profile(request):

    user = CustomUser.objects.get(id = request.user.id)
    
    context = {
        "user": user,
    }

    return render(request, 'profile.html', context)


@login_required(login_url="/")
def update_profile(request):

    if request.method == "POST":
        profile_picture = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_picture

            if password != None and password != "":
                customuser.set_password(password)

            if profile_picture != None and profile_picture != "":
                customuser.profile_pic = profile_picture

            customuser.save()

            messages.success(request, "Profile updated successfully !")
            return redirect('profile_path')


        except:
            messages.error(request, "Profile updation failed !")
            return redirect('profile_path')
    return render(request, "profile.html")
    