# Generated by Django 4.2.3 on 2023-08-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                default=0, max_length=40, unique=True, verbose_name="phone_number"
            ),
            preserve_default=False,
        ),
    ]
