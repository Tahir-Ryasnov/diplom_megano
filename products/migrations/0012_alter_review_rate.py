# Generated by Django 4.2.11 on 2024-05-29 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_alter_review_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Rate",
            ),
        ),
    ]
