# Generated by Django 3.2.6 on 2022-12-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_book_ownerscontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=10, null=True, verbose_name='status'),
        ),
    ]
