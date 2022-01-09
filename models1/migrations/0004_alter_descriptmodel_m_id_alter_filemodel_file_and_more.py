# Generated by Django 4.0.1 on 2022-01-08 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0003_filemodel_file_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptmodel',
            name='m_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models1.kursmodel', verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(blank=True, help_text='Hatoliklar bolmasligi uchun Tanlagan Tipingizdagi filenigina yuklang', null=True, upload_to='static/documents/files'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]