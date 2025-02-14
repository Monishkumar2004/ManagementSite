from django.shortcuts import redirect, render  # Import necessary modules from Django
from django.contrib.auth.decorators import login_required  # Import the login_required decorator

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
    return render(request, 'HOD/add_student.html')