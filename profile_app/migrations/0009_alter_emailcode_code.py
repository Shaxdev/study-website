# Generated by Django 4.0.1 on 2022-01-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0008_alter_emailcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(default='RlLJSXwi', max_length=8),
        ),
    ]
