# Generated by Django 4.1.7 on 2023-04-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHome', '0024_alter_user_to_farmeasy_crop_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_product',
            name='selling_qr_code',
            field=models.ImageField(blank=True, upload_to='selling_qr_image'),
        ),
    ]
