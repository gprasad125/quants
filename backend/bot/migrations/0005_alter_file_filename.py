# Generated by Django 4.1.7 on 2023-03-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_file_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(default='file_from_2023-03-17 19:42:59.385868', max_length=100),
        ),
    ]