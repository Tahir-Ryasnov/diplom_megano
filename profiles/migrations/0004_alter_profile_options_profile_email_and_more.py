# Generated by Django 4.2.11 on 2024-05-01 21:19

from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_alter_avatar_src"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name": "Profile", "verbose_name_plural": "Profiles"},
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, unique=True, verbose_name="email"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ForeignKey(
                default=profiles.models.Avatar.get_default,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to="profiles.avatar",
                verbose_name="Avatar",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="balance",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="balance"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fullName",
            field=models.CharField(max_length=128, verbose_name="full name"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="phone number"
            ),
        ),
    ]
