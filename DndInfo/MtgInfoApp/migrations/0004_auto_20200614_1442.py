# Generated by Django 2.2.13 on 2020-06-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MtgInfoApp', '0003_auto_20200614_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtgcard',
            name='cmc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mtgcard',
            name='multiverse_id',
            field=models.TextField(),
        ),
    ]
