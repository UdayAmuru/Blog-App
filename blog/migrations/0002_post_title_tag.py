# Generated by Django 4.2.2 on 2023-06-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Freakin Awesome Blog!', max_length=290),
        ),
    ]