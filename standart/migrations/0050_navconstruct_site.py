# Generated by Django 3.1.3 on 2020-12-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('standart', '0049_text_examples'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='site',
            field=models.ManyToManyField(blank=True, related_name='site', to='sites.Site'),
        ),
    ]