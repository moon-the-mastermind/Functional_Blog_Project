from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomUser
from django import forms
from django.contrib.auth import get_user_model
from . models import UserProfile

User = get_user_model()


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            "placeholder": "Confirm password"
        })
    )
    class Meta(UserCreationForm.Meta):
        
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "photo", "phone", "password1", "password2"]
        labels = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "username" : "Username",
            "email" : "Email",
            "phone" : "Contact or Phone",
            "password1" : "Enter Password",
            "password2" : "Confirm Password"
        }
        label_classes = {
            "photo" : "block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        }
        widgets = {
            "first_name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Ex. John"
            }),
            "last_name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Ex. Cena"
            }),
            "username" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "@username"
            }),
            "email" : forms.EmailInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "yourmail@example.com"
            }),
            "phone" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "include country code"
            }),

            "photo" : forms.FileInput(attrs={
                "class" : "block w-full text-sm text-gray-700 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",     
            }),

           
            
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            "placeholder" : "@username",
        })
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={
            "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            "placeholder" : "Enter Password",
        })
    )

class UserInProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone", "photo"]
        widgets = {
            "first_name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Ex. John"
            }),
            "last_name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Ex. Cena"
            }),
            "username" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "@username"
            }),
            "email" : forms.EmailInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "yourmail@example.com"
            }),
            "phone" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "include country code"
            }),

            "photo" : forms.FileInput(attrs={
                "class" : "block w-full text-sm text-gray-700 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",     
            }),
            
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ["user"]
        widgets = {
            "bio" : forms.Textarea(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                
            }),
            "address" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Street-village-Thana-District"
            }),
            "date_of_birth" : forms.DateInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "type" : 'date',
            }),
            "facebook_link" : forms.URLInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            }),
            "insta_link" : forms.URLInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",

            }),

            "twitter_link" : forms.URLInput(attrs={
                "class" : "block w-full text-sm text-gray-700 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",     
            }),
            
        }

        

