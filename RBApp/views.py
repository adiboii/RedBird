from django.core.checks import messages
from django.http import request
from django.shortcuts import render
from django.views.generic import View
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import render
# Create your views here.

class MyIndexView(View):
  def get(self,request):
        users = User.objects.all()
        dishes = Dish.objects.all()
        menutype = MenuType.objects.all()
        context = {
            'users': users,
            'dishes': dishes,
            'menutype': menutype
        }
        return render(request, 'index.html', context)


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
        users = User.objects.all()
        dishes = Dish.objects.all()
        menutype = MenuType.objects.all()
        context = {
            'users': users,
            'dishes': dishes,
            'menutype': menutype
        }
        return render(request, 'Dashboard.html', context)


class UserFormView(View):
        def get(self,request):
                return render(request, 'forms/user-form.html', {})
        
        def post(self, request):
                form = UserForm(request.POST)
                if form.is_valid():
                    fname = request.POST.get("first_name")
                    lname = request.POST.get("last_name")
                    uname = request.POST.get("username")
                    pword = request.POST.get("password")
                    pNumber = request.POST.get("phone_number")
                    strt = request.POST.get("street")
                    cty = request.POST.get("city")
                    cntry = request.POST.get("country")
                    form = User(username = uname, password = pword, first_name = fname, last_name = lname, phone_number = pNumber, street = strt, city = cty, country = cntry)
                    form.save()
                    return redirect('RBApp:my_dashboard_view')
                else:
                    messages.error(request, "Error")
                    #return redirect('RBApp:my_dashboard_view')
                




class DishFormView(View):
    def get(self,request):
                return render(request, 'forms/dish-form.html', {})
    def post(self, request):
                form = DishForm(request.POST)
                if form.is_valid():
                    nme = request.POST.get("name")
                    prce = request.POST.get("price")
                    dscrptn = request.POST.get("description")
                    form = Dish(name = nme, price = prce, description = dscrptn)
                    form.save()
                    #return render(request, 'forms/user-form.html', {})
                    return redirect('RBApp:my_dashboard_view')


class MenuTypeFormView(View):
    def get(self,request):
                return render(request, 'forms/menutype-form.html', {})
    def post(self, request):
                form = MenuTypeForm(request.POST)
                if form.is_valid():
                    nme = request.POST.get("name")
                    dscrptn = request.POST.get("description")
                    form = MenuType(name = nme, description = dscrptn)
                    form.save()
                    #return render(request, 'Dashboard.html', {})
                    return redirect('RBApp:my_dashboard_view')