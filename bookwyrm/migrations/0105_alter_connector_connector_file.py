# Generated by Django 3.2.5 on 2021-10-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0104_auto_20211001_2012"),
    ]

    operations = [
        migrations.AlterField(
            model_name="connector",
            name="connector_file",
            field=models.CharField(
                choices=[
                    ("openlibrary", "Openlibrary"),
                    ("inventaire", "Inventaire"),
                    ("bookwyrm_connector", "Bookwyrm Connector"),
                ],
                max_length=255,
            ),
        ),
    ]
