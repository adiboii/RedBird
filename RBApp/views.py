from typing import ContextManager
from django.core.checks import messages
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView
from .forms import *
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
    
    def post(self, request):
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        user = authenticate(request, username = uname, password = pword)

        if user is not None:
            login(request, user)
            return redirect('RBApp:my_index_view')
        else:
            messages.error(request, 'Username or Password do not match')
            return redirect('RBApp:my_login_view')

def logout_view(request):
    logout(request)
    return redirect('RBApp:my_login_view')

class MySignUpView(View):
    def get(self,request):
        return render(request, 'signup.html', {})
        
    def post(self, request):
        uname = request.POST.get("username")
        pNumber = request.POST.get("phone_number")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        pword = request.POST.get("password")
        strt = request.POST.get("street")
        cty = request.POST.get("city")
        cntry = request.POST.get("country")
        if User.objects.filter(username = uname).exists():
            messages.error(request, 'Username already exists')
            return redirect('RBApp:my_signup_view')
        else:
            if str.isnumeric(pNumber):
                user = User.objects.create_user(username = uname,  first_name = fname, last_name = lname, phone_number = pNumber, street = strt, city = cty, country = cntry, password = pword)
                messages.success(request, "User successfully created.")
                return redirect('RBApp:my_login_view')
            else:
                messages.error(request, 'Phone number must contain numbers only')
                return redirect('RBApp:my_signup_view')



class CartView(View):
    def get(self,request):

        if request.user.is_authenticated:
            user = request.user.username
            order, created = Orders.objects.get_or_create(user = user, complete=False)
            items = order.ordereditems_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {
            'items':items,
            'order':order,
            }
        return render(request, 'cart.html', context)



class MyAboutView(View):
     def get(self,request):
        return render(request, 'article.html', {})

class ContactUsView(View):
    def get(self, request):
        return render(request, 'contactus.html', {})

class FeaturesView(View):
    def get(self, request):
        return render(request, 'features.html', {})

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
            uname = request.POST.get("username")
            pNumber = request.POST.get("phone_number")
            fname = request.POST.get("first_name")
            lname = request.POST.get("last_name")
            pword = request.POST.get("password")
            strt = request.POST.get("street")
            cty = request.POST.get("city")
            cntry = request.POST.get("country")
            if User.objects.filter(username = uname).exists():
                messages.error(request, 'Username already exists')
                return redirect('RBApp:my_userform_view')
            else:
                if str.isnumeric(pNumber):
                    user = User.objects.create_user(username = uname,  first_name = fname, last_name = lname, phone_number = pNumber, street = strt, city = cty, country = cntry, password = pword)
                    messages.success(request, "User successfully created.")
                    return redirect('RBApp:my_dashboard_view')
                else:
                    messages.error(request, 'Phone number must contain numbers only')
                    return redirect('RBApp:my_userform_view')
        
                    

class DishFormView(View):
    def get(self,request):
                return render(request, 'forms/dish-form.html', {})
                
    def post(self, request):
                form = DishForm(request.POST)
                nme = request.POST.get("name")
                prce = request.POST.get("price")
                temp = prce.replace(".", "")
                dscrptn = request.POST.get("description")
                if temp.isnumeric():
                    form = Dish(name = nme, price = prce, description = dscrptn)
                    form.save()
                    messages.success(request, "Dish successfully created.")
                    return redirect('RBApp:my_dishform_view')
                else:
                    messages.error(request, "Price must be positive numbers only")
                    return redirect('RBApp:my_dashboard_view')



class MenuTypeFormView(View):
    def get(self,request):
                return render(request, 'forms/menutype-form.html', {})

    def post(self, request):
                form = MenuTypeForm(request.POST)
                if form.is_valid():
                    nme = request.POST.get("name")
                    dscrptn = request.POST.get("description")
                    if MenuType.objects.filter(name = nme).exists():
                        messages.error(request, 'Menu Type already exists')
                        return redirect('RBApp:my_menutypeform_view"')
                    else:
                        form = MenuType(name = nme, description = dscrptn)
                        form.save()
                        #return render(request, 'Dashboard.html', {})
                        messages.success(request, "Menu Type successfully created.")
                        return redirect('RBApp:my_dashboard_view')

def delete_user(request, username):
    obj = User.objects.get(username = username)
    obj.delete()
    return redirect('RBApp:my_dashboard_view')

def delete_dish(request, dish_id):
    dish = Dish.objects.get(dish_id = dish_id)
    dish.delete()
    return redirect('RBApp:my_dashboard_view')

def delete_menu_type(request, type_id):
    menu_type = MenuType.objects.get(type_id = type_id)
    menu_type.delete()
    return redirect('RBApp:my_dashboard_view')

def edit_user(request, username):
    template = 'forms/edit-user.html'
    user = User.objects.get(username = username)

    if request.method == "POST":
        form = UserForm(request.POST)
        uname = request.POST.get("username")
        pNumber = request.POST.get("phone_number")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        pword = request.POST.get("password")
        strt = request.POST.get("street")
        cty = request.POST.get("city")
        cntry = request.POST.get("country")
        try:
            # update_user = User.objects.filter(username = uname).update(password = pword, first_name = fname, last_name = lname, phone_number = pNumber, street = strt, city = cty, country = cntry)
            # print(update_user)
            update_user = User.objects.update_user(username = uname,  first_name = fname, last_name = lname, phone_number = pNumber, street = strt, city = cty, country = cntry, password = pword)
            messages.success(request, 'User has been updated.')
            

        except Exception as e:
            messages.warning(request, 'User was not saved due to error: {}'.format(e))
        
        return redirect('RBApp:my_dashboard_view')
    
    else:
        form = UserForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    
    return render(request, template, context)



def edit_dish(request, dish_id):
    template = 'forms/edit-dish.html'
    dish = Dish.objects.get(dish_id = dish_id)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        nme = request.POST.get("name")
        prce = request.POST.get("price")
        temp = prce.replace(".", "")
        dscrptn = request.POST.get("description")
        if temp.isnumeric():
            try:
                update_dish = Dish.objects.filter(dish_id = dish_id).update(name = nme, price = prce, description = dscrptn)
                print(update_dish)
                messages.success(request, 'Dish has been updated.')
                
                    
            except Exception as e:
                messages.warning(request, 'Dish was not saved due to error: {}'.format(e))

            return redirect('RBApp:my_dashboard_view')
    
    else:
        form = DishForm(instance=dish)

    context = {
        'form': form,
        'dish': dish,
    }
    
    return render(request, template, context)



def edit_menu_type(request, type_id):
    template = 'forms/edit-type.html'
    type = MenuType.objects.get(type_id = type_id)
    if request.method == "POST":
        form = MenuTypeForm(request.POST, instance=type)
        nme = request.POST.get("name")
        dscrptn = request.POST.get("description")
        form = MenuType(name = nme, description = dscrptn)
        try:
            update_menu_type = MenuType.objects.filter(type_id = type_id).update(name = nme, description = dscrptn)
            print(update_menu_type)
            messages.success(request, 'Menu Type has been updated.')
            return redirect('RBApp:my_dashboard_view')
                
        except Exception as e:
            messages.warning(request, 'Menu Type was not saved due to error: {}'.format(e))
        
        return redirect('RBApp:my_dashboard_view')
    
    else:
        form = MenuTypeForm(instance=type)

    context = {
        'form': form,
        'type': type,
    }
    
    return render(request, template, context)



