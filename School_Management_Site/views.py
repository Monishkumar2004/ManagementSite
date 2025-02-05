from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
def base(request):
    return render(request, "base.html")

def login_view(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method == "POST":
        # user = EmailBackend.authenticate(
        # Django automatically uses the authentication backends defined in your settings.py. EmailBackend model registed in Athentication_backend in settings.py
        user = authenticate(
            request,
            username = request.POST.get("email"),
            password = request.POST.get("password"),
        )

        if user != None:
            login(request, user)
            user_type = user.user_type
            
            if user_type == '1':
                return HttpResponse("This is admin panel")
            elif user_type == '2':
                return HttpResponse("This is staff panel")
            elif user_type == '3':
                return HttpResponse("This is student panel")
            else:
                # If the password is wrong but the user exists we redirect the user to the login page again
                return redirect('login')
        
        else:
            return redirect('login')