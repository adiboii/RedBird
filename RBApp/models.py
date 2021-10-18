from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.class Cart(models.Model):


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256)
    total_price = models.FloatField()

    class meta:
        db_table = 'Cart'


class CartItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    cart_id = models.IntegerField()

    class meta:
        db_table = 'CartItem'


class ItemsInCart(models.Model):
    seq_id = models.AutoField(primary_key=True)  # counter attribute
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    class meta:
        db_table = 'ItemsInCart'


class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, phone_number,  street, city, country, password=None, is_staff = False, is_admin = False):

        if not username:
            raise ValueError('You must provide a username')
        if not password:
            raise ValueError('You must provide a password')
        if not first_name:
            raise ValueError('You must provide a first name')
        if not last_name:
            raise ValueError('You must provide a last name')
        if not phone_number:
            raise ValueError('You must provide a phone number')
        if not street:
            raise ValueError('You must provide a street')
        if not city:
            raise ValueError('You must provide a city')
        if not country:
            raise ValueError('You must provide a country')

        user = self.model(username=username, first_name=first_name, last_name=last_name, phone_number=phone_number, street=street, city=city, country=country)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.save()
        return user
    
    def create_staffuser(self, username, first_name, last_name, phone_number,  street, city, country, password=None):
        user = self.create_user(username, first_name, last_name, phone_number,  street, city, country, password=password, is_staff=True)
        return user
        
    def create_superuser(self, username, first_name, last_name, phone_number,  street, city, country, password=None):
        user = self.create_user(username, first_name, last_name, phone_number,  street, city, country, password=password, is_staff=True, is_admin=True)
        return user
     



class User(AbstractBaseUser):
    username = models.CharField(max_length=256, primary_key=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'street', 'city', 'country']

    def __str__(self):
        return self.username

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(seslf, app_label):
        return True
    
    @property 
    def is_staff(self):
        return self.staff

    @property 
    def is_admin(self):
        return self.admin

    
    class meta:
        db_table = 'User'


class CartToUser(models.Model):
    seq_id = models.AutoField(primary_key=True)  # counter attribute
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class meta:
        db_table = 'CartToUser'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=11)
    total_price = models.FloatField()

    class meta:
        db_table = 'Order'


class OrderedItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    class meta:
        db_table = 'OrderedItems'


class UserToOrder(models.Model):
    seq_id = models.AutoField(primary_key=True)  # counter attribute
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        db_table = 'UserToOrder'


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    image_location = models.CharField(max_length=255, default='')

    class meta:
        db_table = 'Dish'


class DishToCartItem(models.Model):
    seq_id = models.AutoField(primary_key=True)  # counter attribute
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    item_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    class meta:
        db_table = 'DishToCartItem'


class MenuType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)

    class meta:
        db_table = 'MenuType'


class DishType(models.Model):
    seq_id = models.AutoField(primary_key=True)  # counter attribute
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    type_id = models.ForeignKey(MenuType, on_delete=models.CASCADE)

    class meta:
        db_table = 'DishType'
