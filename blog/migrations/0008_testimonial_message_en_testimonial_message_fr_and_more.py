# Generated by Django 4.2.11 on 2024-03-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_testimonial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonial",
            name="message_en",
            field=models.TextField(null=True, verbose_name="Message"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="message_fr",
            field=models.TextField(null=True, verbose_name="Message"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="message_km",
            field=models.TextField(null=True, verbose_name="Message"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="role_en",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Role"
            ),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="role_fr",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Role"
            ),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="role_km",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Role"
            ),
        ),
    ]
