# Generated by Django 4.0.1 on 2022-01-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0014_rename_documents_docmodels_documentfile_document_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentcontent',
            name='document_id',
        ),
        migrations.RemoveField(
            model_name='documentfile',
            name='document_id',
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_type',
            field=models.CharField(choices=[('Prezintatsiya', 'Prezintatsiya'), ('Video', 'Video'), ('Documents', 'Documents')], help_text='File turini tanlang', max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='DOCMODELS',
        ),
        migrations.DeleteModel(
            name='DocumentContent',
        ),
        migrations.DeleteModel(
            name='DocumentFile',
        ),
    ]
