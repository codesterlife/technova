# Generated by Django 4.2.6 on 2024-01-16 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level_one', '0009_alter_imgmodel_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImgModel',
            new_name='ImgQuestion',
        ),
    ]
