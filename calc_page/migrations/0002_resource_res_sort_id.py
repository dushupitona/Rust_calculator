# Generated by Django 4.2.5 on 2023-09-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='res_sort_id',
            field=models.IntegerField(default=0),
        ),
    ]