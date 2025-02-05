from django.shortcuts import render, redirect, HttpResponse  # Import necessary functions for rendering and redirecting
from app.EmailBackend import EmailBackend  # Import the custom EmailBackend for authentication
from django.contrib.auth import authenticate, login, logout  # Import authentication functions

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
                return HttpResponse("This is admin panel")
            elif user_type == '2':  # If user is Staff
                return HttpResponse("This is staff panel")
            elif user_type == '3':  # If user is Student
                return HttpResponse("This is student panel")
            else:
                return redirect('login')  # Redirect to login if user type is unrecognized
        
        else:
            return redirect('login')  # Redirect to login if authentication failed
