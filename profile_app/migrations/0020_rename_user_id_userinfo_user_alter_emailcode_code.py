# Generated by Django 4.0.1 on 2022-01-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0019_rename_user_emailcode_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(default='zwnqcASA', max_length=8),
        ),
    ]