from django.db import models

# Create your models here.

# CREATE TABLE User(
# 	username varchar(256) NOT NULL,
# 	first_name varchar(256),
# 	last_name varchar(256),
# 	phone_number varchar(11),
# 	street varchar(30),
# 	city varchar(30),
# 	country varchar(11),
# 	PRIMARY KEY(username)
# );	


class User(models.Model):
    username = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 11)
    street = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    
    class meta:
        db_table = 'User'

#CREATE TABLE Cart(
# 	cart_id int NOT NULL AUTO_INCREMENT,
# 	username varchar(256),
# 	total_price float(6, 2),
# 	PRIMARY KEY(cart_id),
# 	FOREIGN KEY(username) REFERENCES User(username)
# );


class Cart(models.Model):
    cart_id = models.IntegerField()
    username = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    total_price = models.FloatField()


# CREATE TABLE Order(
# 	order_id int NOT NULL AUTO_INCREMENT,
# 	username varchar(256),
# 	street varchar(30),
# 	city varchar(30),
# 	country varchar(11),
# 	phone_number varchar(11),
# 	total_price float(6, 2),
# 	PRIMARY KEY(order_id),
# 	FOREIGN KEY(username) REFERENCES User(username)
# );


class Order(models.Model):
    order_id = models.IntegerField()
    username = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    street = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    city = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    country = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    phone_number = models.ForeignKey(User, on_delete = models.CASCADE, on_update = models.CASCADE)
    total_price = models.ForeignKey(Cart, on_delete = models.CASCADE, on_update = models.CASCADE)

# CREATE TABLE MenuType(
#  type_id int NOT NULL AUTO_INCREMENT,
#  name varchar(256),
#  description varchar(256),
#  PRIMARY KEY(type_id)
# );

class MenuType(models.Model):
    type_id = models.IntegerField()
    name = models.CharField()
    description = models.CharField()


# CREATE TABLE Dish(
#  dish_id int NOT NULL AUTO_INCREMENT,
#  name varchar(256),
#  price float(5, 2),
#  description varchar(256),
#  type_id int, 
#  PRIMARY KEY(dish_id),
#  FOREIGN KEY(type_id) REFERENCES MenuType(type_id)
# );

class Dish(models.Model):
    dish_id = models.IntegerField()
    name = models.CharField()
    price = models.FloatField()
    description = models.CharField()
    type_id =  models.ForeignKey(MenuType, on_delete = models.CASCADE, on_update = models.CASCADE)

# CREATE TABLE CartItem(
#  item_id int NOT NULL AUTO_INCREMENT,
#  dish_id int,
#  quantity int,
#  total_price float(6, 2),
#  PRIMARY KEY(item_id),
#  FOREIGN KEY(dish_id) REFERENCES Dish(dish_id)
# );


class CartItem(models.Model):
    item_id = models.IntegerField()
    dish_id =  models.ForeignKey(Dish, on_delete = models.CASCADE, on_update = models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    