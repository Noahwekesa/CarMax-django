from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


def profile(request):
    return render(request, 'users/profiles')


def logout_view(request):
    logout(request)
    messages.success(request, "You Ended Your Session")
    return redirect('login')


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    success_message = "Your Account Was Created Successfully!"
