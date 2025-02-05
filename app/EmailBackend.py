from django.contrib.auth import get_user_model  # Import function to get the custom user model
from django.contrib.auth.backends import ModelBackend  # Import base authentication backend class


class EmailBackend(ModelBackend):  # Custom authentication backend class
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Custom authentication method to allow login using email instead of username.
        """
        UserModel = get_user_model()  # Get the user model (CustomUser if defined)
        
        try:
            # Try to get the user by their email
            user = UserModel.objects.get(email=username)  
        except UserModel.DoesNotExist:
            # If no user is found with the given email, return None (authentication failed)
            return None
        else:
            # If user exists, check if the provided password matches the stored password
            if user.check_password(password):  
                return user  # Authentication successful, return the user object
        
        return None  # Authentication failed, return None
