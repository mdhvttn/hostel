from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)



class AddYear(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'
        labels = {
            "year" : "Enter year you want to add"
        }
        widgets = {
            'year': forms.TextInput(attrs={'placeholder': 'Should be unique'}),
        }

class AddStudent(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__' 
        # error_message = {
        #     'phone' : {
        #         "unique":'phone is already register'
        #     }
        # }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Length should be 10'}),
        }

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    #when we do form.is_valid it will always run clean function
    def clean(self,*args,**kwargs):
            username = self.cleaned_data.get("username")
            password = self.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            user_qs = User.objects.filter(username=username)

            if user_qs.count()==1:
                user = user_qs.first()
            if not user:
                raise forms.ValidationError("This user does not exist!!")
            if not user.check_password(password):
                raise forms.ValidationError("Password is incorrect !!")
            if not user.is_active:
                raise forms.ValidationError("This User is not longer active")
            return super(UserLoginForm,self).clean(*args,**kwargs)