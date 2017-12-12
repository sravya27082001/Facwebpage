from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
	)

    def save(self, commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        if commit:
            user.save()

        return user
#class EditProfileForm(UserChangeForm):

  #  class Meta:
 #       model=User
   #     fields=(
    #        "email",
     #       "first_name",
      #      "last_name",
       #     "password"
       # )
#class UserForm(forms.ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput)

#    class Meta:
 #       model = User
  #      fields = ['username','email','password']
