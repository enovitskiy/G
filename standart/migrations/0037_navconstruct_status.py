# Generated by Django 3.1.3 on 2020-12-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0036_subnavigator_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='status',
            field=models.CharField(choices=[('odinary', 'Odinary'), ('form', 'Form'), ('example', 'Example')], default='odinary', max_length=10),
        ),
    ]
