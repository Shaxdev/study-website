# Generated by Django 4.0.1 on 2022-01-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0005_emailcode_alter_userinfo_options_delete_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(default='xP1kEkYw', max_length=8),
        ),
    ]