# Import necessary functions for rendering and redirecting
from django.shortcuts import render, redirect, HttpResponse  

# Import the custom EmailBackend for authentication
from app.EmailBackend import EmailBackend  

# Import authentication functions
from django.contrib.auth import authenticate, login, logout  

# Import messages module for displaying alerts
from django.contrib import messages

# Import login_required decorator for restricting access to certain pages
from django.contrib.auth.decorators import login_required  

# Import the CustomUser model
from app.models import CustomUser


def base(request):
    """
    Render the base template.
    """
    # Render the base.html template
    return render(request, "base.html")  


def login_view(request):
    """
    Render the login page.
    """
    # Render the login.html template
    return render(request, "login.html")  


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
                # Display error message if user type is unrecognized
                messages.error(request, "Email and Password Invalid !")
                return redirect('login_path')  # Redirect to login if user type is unrecognized
        
        else:
            # Display error message if authentication failed
            messages.error(request, "Email and Password Invalid !")
            return redirect('login_path')  # Redirect to login if authentication failed
        

def doLogout(request):
    # Log out the user
    logout(request)
    # Redirect to the login page after logout
    return redirect('login_path')


# Profile Views
@login_required(login_url="/")  # Ensure only logged-in users can access this view
def profile(request):
    # Get the current user
    user = CustomUser.objects.get(id=request.user.id)
    
    # Create a context dictionary with the user object
    context = {
        "user": user,
    }

    # Render the profile.html template with the user context
    return render(request, 'profile.html', context)


@login_required(login_url="/")  # Ensure only logged-in users can access this view
def update_profile(request):
    if request.method == "POST":  # Check if the request method is POST
        # Get the new profile picture from the request
        profile_picture = request.FILES.get("profile_pic")
        
        # Get other updated fields from the request
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        

        try:
            # Get the current user
            customuser = CustomUser.objects.get(id=request.user.id)
            
            # Update user fields
            customuser.first_name = first_name
            customuser.last_name = last_name
            
            # Update profile picture if provided
            if profile_picture != None and profile_picture != "":
                customuser.profile_pic = profile_picture

            # Update password if provided
            if password != None and password != "":
                customuser.set_password(password)

            # Save the changes
            customuser.save()

            # Display success message
            messages.success(request, "Profile updated successfully !")
            return redirect('profile_path')

        except:
            # Display error message if profile update fails
            messages.error(request, "Profile updation failed !")
            return redirect('profile_path')
    
    # If not a POST request, render the profile.html template for editing
    return render(request, "profile.html")
