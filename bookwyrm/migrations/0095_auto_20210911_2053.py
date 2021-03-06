# Generated by Django 3.2.4 on 2021-09-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0094_auto_20210911_1550"),
    ]

    operations = [
        migrations.AlterField(
            model_name="connector",
            name="deactivation_reason",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pending", "Pending"),
                    ("self_deletion", "Self deletion"),
                    ("moderator_suspension", "Moderator suspension"),
                    ("moderator_deletion", "Moderator deletion"),
                    ("domain_block", "Domain block"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="deactivation_reason",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pending", "Pending"),
                    ("self_deletion", "Self deletion"),
                    ("moderator_suspension", "Moderator suspension"),
                    ("moderator_deletion", "Moderator deletion"),
                    ("domain_block", "Domain block"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
