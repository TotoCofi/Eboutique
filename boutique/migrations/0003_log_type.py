# Generated by Django 4.2.2 on 2023-06-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='type',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
