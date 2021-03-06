# Generated by Django 3.2.10 on 2022-01-10 21:20

import bookwyrm.models.activitypub_mixin
import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0125_alter_user_preferred_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="LinkDomain",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "remote_id",
                    bookwyrm.models.fields.RemoteIdField(
                        max_length=255,
                        null=True,
                        validators=[bookwyrm.models.fields.validate_remote_id],
                    ),
                ),
                ("domain", models.CharField(max_length=255, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("approved", "Approved"),
                            ("blocked", "Blocked"),
                            ("pending", "Pending"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "reported_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "remote_id",
                    bookwyrm.models.fields.RemoteIdField(
                        max_length=255,
                        null=True,
                        validators=[bookwyrm.models.fields.validate_remote_id],
                    ),
                ),
                ("url", bookwyrm.models.fields.URLField(max_length=255)),
                (
                    "added_by",
                    bookwyrm.models.fields.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "domain",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="bookwyrm.linkdomain",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(bookwyrm.models.activitypub_mixin.ActivitypubMixin, models.Model),
        ),
        migrations.CreateModel(
            name="FileLink",
            fields=[
                (
                    "link_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bookwyrm.link",
                    ),
                ),
                ("filetype", bookwyrm.models.fields.CharField(max_length=5)),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="file_links",
                        to="bookwyrm.book",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("bookwyrm.link",),
        ),
    ]
