# Generated by Django 3.1.3 on 2020-12-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0014_auto_20201216_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
