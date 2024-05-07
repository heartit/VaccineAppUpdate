# Generated by Django 4.2.11 on 2024-04-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_post_title_post_juza_post_reader_post_surah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='language',
        ),
        migrations.RemoveField(
            model_name='record',
            name='shiek',
        ),
        migrations.AddField(
            model_name='record',
            name='reader',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='juza',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='surah',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]