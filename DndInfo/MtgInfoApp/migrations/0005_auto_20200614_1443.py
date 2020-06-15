# Generated by Django 2.2.13 on 2020-06-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MtgInfoApp', '0004_auto_20200614_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtgcard',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='border',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='color_identity',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='flavor',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='foreign_names',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='hand',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='legalities',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='life',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='loyalty',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='multiverse_id',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='names',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='number',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='original_text',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='original_type',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='power',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='printings',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='rulings',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='set',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='set_name',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='source',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='starter',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='subtypes',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='supertypes',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='text',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='timeshifted',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='toughness',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='type',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='variations',
        ),
        migrations.RemoveField(
            model_name='mtgcard',
            name='watermark',
        ),
        migrations.AlterField(
            model_name='mtgcard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]