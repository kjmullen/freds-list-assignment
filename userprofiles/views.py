from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

class RegisterUser(CreateView):

    model = User
    form_class = UserCreationForm