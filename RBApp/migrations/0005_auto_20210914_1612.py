# Generated by Django 3.2.6 on 2021-09-14 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RBApp', '0004_dish_image_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image_location',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='type_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RBApp.cartitem')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RBApp.order')),
            ],
        ),
    ]
