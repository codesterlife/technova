# Generated by Django 4.2.6 on 2024-01-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_one', '0014_mcqquestion_img_mcqquestion_img_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnaquestion',
            name='img',
            field=models.ImageField(blank=True, height_field='img_height', null=True, upload_to='img_quiz', width_field='img_width'),
        ),
        migrations.AddField(
            model_name='qnaquestion',
            name='img_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qnaquestion',
            name='img_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
