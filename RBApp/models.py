from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 100, primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 11)
    street = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    
    class meta:
        db_table = 'User'

    def __str__(self):
        return self.name

class MenuType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    # image_location = models.CharField(max_length=255)
    type_id =  models.ForeignKey(MenuType, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    total_price = models.FloatField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    dish_id =  models.ForeignKey(Dish, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    cart_id = models.ForeignKey(Cart, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(CartItem, on_delete = models.CASCADE)
    username = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_item_id')
    street = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_username')
    city = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_city')
    country = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_country')
    phone_number = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_phone_number')
    total_price = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name='oder_total_price')

    def __str__(self):
        return self.name