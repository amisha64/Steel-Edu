# Generated by Django 4.0.5 on 2022-06-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_data_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='country',
            field=models.PositiveIntegerField(choices=[(1, 'India')], null=True),
        ),
    ]
