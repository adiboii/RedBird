from django.http import request
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class MyIndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class MyLoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})
        
class MySignUpView(View):
       def get(self,request):
        return render(request, 'signup.html', {})

class MyAboutView(View):
     def get(self,request):
        return render(request, 'article.html', {})

        
class MyDashboardView(View):
     def get(self,request):
        return render(request, 'Dashboard.html', {})
