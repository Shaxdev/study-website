# Generated by Django 4.0.1 on 2022-01-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0006_filemodel_position_fmodel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='position',
        ),
        migrations.RemoveField(
            model_name='inlinemodelcontent',
            name='position',
        ),
        migrations.AddField(
            model_name='insidemodel',
            name='position',
            field=models.PositiveIntegerField(null=True),
        ),
    ]