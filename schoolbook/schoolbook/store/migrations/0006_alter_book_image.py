# Generated by Django 3.2.6 on 2022-12-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/% Y/% m/% d/'),
        ),
    ]
