# Generated by Django 2.2.28 on 2023-03-28 04:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("crapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="transaction_id",
            field=models.CharField(default=uuid.uuid4, max_length=255),
        ),
    ]
