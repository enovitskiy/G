# Generated by Django 3.1.3 on 2020-12-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0046_auto_20201216_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navconstructtranslation',
            name='hreflogo',
            field=models.TextField(blank=True, help_text='текст блока', max_length=100, verbose_name='Текст блока'),
        ),
    ]
