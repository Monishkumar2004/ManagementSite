from django.contrib.auth import get_user_model  # Import function to get the custom user model
from django.contrib.auth.backends import ModelBackend  # Import base authentication backend class

class EmailBackend(ModelBackend):  # Custom authentication backend class
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Custom authentication method to allow login using email instead of username.
        """
        UserModel = get_user_model()  # Get the user model (CustomUser if defined)
        
        try:
            # Attempt to retrieve the user by their email address
            user = UserModel.objects.get(email=username)  
        except UserModel.DoesNotExist:
            # If no user is found with the given email, return None (authentication failed)
            return None
        else:
            # If the user exists, verify if the provided password matches the stored password
            if user.check_password(password):  
                return user  # Authentication successful; return the user object
        
        return None  # If password check fails, return None (authentication failed)
