# Generated by Django 4.0.1 on 2022-01-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0015_alter_emailcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(default='6zkiU12N', max_length=8),
        ),
    ]
