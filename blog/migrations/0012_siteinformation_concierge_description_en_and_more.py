# Generated by Django 4.2.11 on 2024-03-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_siteinformation"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteinformation",
            name="concierge_description_en",
            field=models.TextField(
                help_text="Description of the concierge company services.",
                null=True,
                verbose_name="Concierge Company Description",
            ),
        ),
        migrations.AddField(
            model_name="siteinformation",
            name="concierge_description_fr",
            field=models.TextField(
                help_text="Description of the concierge company services.",
                null=True,
                verbose_name="Concierge Company Description",
            ),
        ),
        migrations.AddField(
            model_name="siteinformation",
            name="concierge_description_km",
            field=models.TextField(
                help_text="Description of the concierge company services.",
                null=True,
                verbose_name="Concierge Company Description",
            ),
        ),
    ]
