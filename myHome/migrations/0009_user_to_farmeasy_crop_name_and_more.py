# Generated by Django 4.1.7 on 2023-03-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHome', '0008_user_to_farmeasy_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_to_farmeasy',
            name='crop_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_to_farmeasy',
            name='crop_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
