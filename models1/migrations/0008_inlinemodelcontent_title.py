# Generated by Django 4.0.1 on 2022-01-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0007_remove_filemodel_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinemodelcontent',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]