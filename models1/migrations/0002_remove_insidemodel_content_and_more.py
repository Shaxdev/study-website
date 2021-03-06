# Generated by Django 4.0.1 on 2022-01-08 11:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insidemodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='insidemodel',
            name='document',
        ),
        migrations.RemoveField(
            model_name='insidemodel',
            name='video',
        ),
        migrations.AlterField(
            model_name='descriptmodel',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kursmodel',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Qoshilgan vaqti'),
        ),
        migrations.CreateModel(
            name='InlineModelContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('inside_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models1.insidemodel')),
            ],
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(null=True)),
                ('file_type', models.CharField(choices=[('Prezintatsiya', 'Prezintatsiya'), ('Document', 'Document'), ('Video', 'Video')], help_text='File turini tanlang', max_length=15, null=True)),
                ('file', models.FileField(help_text='Hatoliklar bolmasligi uchun Tanlagan Tipingizdagi filenigina yuklang', null=True, upload_to='static/documents/files')),
                ('inside_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models1.insidemodel')),
            ],
        ),
    ]
