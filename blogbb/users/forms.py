from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationFrom(UserCreationForm):

    # email=forms.EmailField()

    email = forms.EmailField(required=True, label="Email:",
                             widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                           'autocomplete': 'off',
                                                           'size': '40',
                                                           'font-size': 'xx-large',
                                                           }))
    username = forms.CharField(required=True, label="Username:",widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                           'autocomplete': 'off',
                                                           'size': '40',
                                                           'font-size': 'xx-large',
                                                           }))
    first_name = forms.CharField(required=True, label="First Name:",widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                           'autocomplete': 'off',
                                                           'size': '40',
                                                           'font-size': 'xx-large',
                                                           }))
    last_name = forms.CharField(label="Last Name:",widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                           'autocomplete': 'off',
                                                           'size': '40',
                                                           'font-size': 'xx-large',
                                                           }))
    password1 = forms.CharField(widget=forms.PasswordInput, required=True,
                                label="Password:"
                                )
    password2 = forms.CharField(widget=forms.PasswordInput, required=True,
                                label="Confirm Password:")


    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

    def clean_email(self):   # validate email
        email=self.cleaned_data.get("email")
        user_count=User.objects.filter(email=email).count()
        print(user_count)
        if user_count>0:
            raise forms.ValidationError("email is already existed, try with another email")
        return email


