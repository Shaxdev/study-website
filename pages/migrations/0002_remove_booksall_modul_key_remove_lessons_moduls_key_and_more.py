# Generated by Django 4.0.1 on 2022-01-09 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0010_remove_fmodel_inside_model_remove_korishlar_model_id_and_more'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksall',
            name='modul_key',
        ),
        migrations.RemoveField(
            model_name='lessons',
            name='moduls_key',
        ),
        migrations.RemoveField(
            model_name='moduls',
            name='users',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterField(
            model_name='testmodul',
            name='moduls_test_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models1.mainmodel', verbose_name='Test Moduli'),
        ),
        migrations.AlterField(
            model_name='testmodul',
            name='time_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='booksall',
        ),
        migrations.DeleteModel(
            name='lessons',
        ),
        migrations.DeleteModel(
            name='Moduls',
        ),
    ]
