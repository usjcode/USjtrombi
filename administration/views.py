from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

class LoginView(FormView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form_class = LoginForm
    success_url="/"
    def form_valid(self, form):
        username=self.request.POST["username"]
        password=self.request.POST["password"]
        print(username,password)
        user = authenticate(username=username,password=password)
        login(self.request,user)
        if next in self.request.GET.keys():
            return redirect(self.request.GET["next"])
        return super().form_valid(form)