# Generated by Django 3.1.3 on 2020-12-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0044_templatecategory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metkatranslation',
            name='title',
            field=models.CharField(blank=True, help_text='категория проекта', max_length=100, verbose_name='Категория проекта'),
        ),
    ]
