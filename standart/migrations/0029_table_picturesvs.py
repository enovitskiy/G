# Generated by Django 3.1.3 on 2020-12-03 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0028_auto_20201203_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='picturesvs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablevs', to='standart.pictures'),
        ),
    ]
