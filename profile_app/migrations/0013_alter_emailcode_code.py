# Generated by Django 3.2.9 on 2022-01-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0012_alter_emailcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(default='OQATOFKT', max_length=8),
        ),
    ]
