# Generated by Django 3.1.3 on 2020-12-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0020_auto_20201202_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examples',
            options={'verbose_name': 'Пример', 'verbose_name_plural': 'Примеры'},
        ),
        migrations.AlterModelOptions(
            name='examplestranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Пример Translation'},
        ),
        migrations.AddField(
            model_name='examples',
            name='marks',
            field=models.ManyToManyField(blank=True, null=True, related_name='marks', to='standart.Metka'),
        ),
    ]