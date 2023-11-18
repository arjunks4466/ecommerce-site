from django import forms
from django.contrib.auth.models import User
from .models import*
from django.views import generic
from django.urls import reverse_lazy


# class userreg(forms.Form):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password']



class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    conf=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','conf']

class userlogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

# __all__ constructor
# __all__ is a field that indicates all fields in model should be included in from
# __all__  return a list of model fields

class regform(forms.ModelForm):
    class Meta:
        model= regmodel
        fields= '__all__'

class register(generic.CreateView):
    form_class=regform
    template_name = 'register.html'
    success_url = reverse_lazy('login1')  # reverse_lazy - it is used to imply a lazy implementation of url used to redirect

class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


# class userreg(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']







# class logform1(forms.Form):
#     username=forms.CharField(max_length=50)
#     password=forms.CharField(max_length=50)



class userreg(forms.ModelForm):
    conf=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class u_login(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)


class UserListView(generic.ListView):
    model = regmodel
    template_name = 'disp.html'
    context_object_name = 'user_list'

class imageform(forms.ModelForm):
    class Meta:
        model=imageupload
        fields= '__all__'


class filesupload(forms.ModelForm):
    class Meta:
        model = fileuploads_model
        fields = '__all__'


