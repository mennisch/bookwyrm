# Generated by Django 3.2.4 on 2021-08-16 20:22

import bookwyrm.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0082_auto_20210806_2324"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="reading_status",
            field=bookwyrm.models.fields.CharField(
                blank=True,
                choices=[
                    ("to-read", "Toread"),
                    ("reading", "Reading"),
                    ("read", "Read"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="quotation",
            name="reading_status",
            field=bookwyrm.models.fields.CharField(
                blank=True,
                choices=[
                    ("to-read", "Toread"),
                    ("reading", "Reading"),
                    ("read", "Read"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="reading_status",
            field=bookwyrm.models.fields.CharField(
                blank=True,
                choices=[
                    ("to-read", "Toread"),
                    ("reading", "Reading"),
                    ("read", "Read"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
