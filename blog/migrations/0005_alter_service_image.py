# Generated by Django 4.2.11 on 2024-03-16 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_service_description_en_service_description_fr_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="image",
            field=models.ImageField(upload_to="static/images/"),
        ),
    ]
