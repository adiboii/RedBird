from django.db import models

# Create your models here.class Cart(models.Model):
class Cart(models.Model):
	cart_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 256)
	total_price = models.FloatField()

	class meta:
		db_table = 'Cart'

class CartItem(models.Model):
	item_id = models.AutoField(primary_key = True)
	quantity = models.IntegerField()
	total_price = models.FloatField()
	cart_id = models.IntegerField()

	class meta:
		db_table = 'CartItem'

class ItemsInCart(models.Model):
	seq_id = models.AutoField(primary_key=True) # counter attribute
	cart_id = models.ForeignKey(Cart, on_delete = models.CASCADE)
	item_id = models.ForeignKey(CartItem, on_delete = models.CASCADE)

	class meta:
		db_table = 'ItemsInCart'

class User(models.Model):
    username = models.CharField(max_length = 256, primary_key = True)
    password = models.CharField(max_length = 256)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 11)
    street = models.CharField(max_length = 256)
    city = models.CharField(max_length = 256)
    country = models.CharField(max_length = 256)

    class meta:
        db_table = 'User'

class CartToUser(models.Model):
	seq_id = models.AutoField(primary_key=True) # counter attribute
	username = models.ForeignKey(User, on_delete = models.CASCADE)
	cart_id = models.ForeignKey(Cart, on_delete = models.CASCADE)

	class meta:
		db_table = 'CartToUser'

class Order(models.Model):
	order_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 256)
	street = models.CharField(max_length = 256)
	city = models.CharField(max_length = 256)
	country = models.CharField(max_length = 256)
	phone_number = models.CharField(max_length = 11)
	total_price = models.FloatField()

	class meta:
		db_table = 'Order'

class OrderedItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    item_id = models.ForeignKey(CartItem, on_delete = models.CASCADE)
  
    class meta:
        db_table = 'OrderedItems'

class UserToOrder(models.Model):
	seq_id = models.AutoField(primary_key=True) # counter attribute
	order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
	username = models.ForeignKey(User, on_delete = models.CASCADE)

	class meta:
		db_table = 'UserToOrder'

class Dish(models.Model):
    dish_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.CharField(max_length = 1000)
    image_location = models.CharField(max_length=255, default='')
    
    class meta:
        db_table = 'Dish'

class DishToCartItem(models.Model):
	seq_id = models.AutoField(primary_key=True) # counter attribute
	dish_id = models.ForeignKey(Dish, on_delete = models.CASCADE)
	item_id = models.ForeignKey(CartItem, on_delete = models.CASCADE)

	class meta:
		db_table = 'DishToCartItem'

class MenuType(models.Model):
	type_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 256)
	description = models.CharField(max_length = 1000)

	class meta:
		db_table = 'MenuType'

class DishType(models.Model):
	seq_id = models.AutoField(primary_key=True) # counter attribute
	dish_id = models.ForeignKey(Dish, on_delete = models.CASCADE)
	type_id = models.ForeignKey(MenuType, on_delete = models.CASCADE)

	class meta:
		db_table = 'DishType'