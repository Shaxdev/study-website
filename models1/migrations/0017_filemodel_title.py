# Generated by Django 4.0.1 on 2022-01-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0016_filemodel_downloadable'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
