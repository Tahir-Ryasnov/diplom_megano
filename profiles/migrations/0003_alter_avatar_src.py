# Generated by Django 4.2.11 on 2024-05-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avatar",
            name="src",
            field=models.ImageField(
                default="app_profiles/avatars/default.jpg",
                upload_to="app_profiles/avatars/user_avatars/",
                verbose_name="Link",
            ),
        ),
    ]
