# Generated by Django 4.2.6 on 2024-02-11 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_visited_level3_task4_visitedtasks_visited_level3_clue4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitedtasks',
            old_name='visited_level5_task1',
            new_name='visited_level5_task',
        ),
        migrations.RenameField(
            model_name='visitedtasks',
            old_name='visited_level3_clue1',
            new_name='visited_level5_task_clue1',
        ),
        migrations.RenameField(
            model_name='visitedtasks',
            old_name='visited_level3_clue2',
            new_name='visited_level5_task_clue2',
        ),
        migrations.RenameField(
            model_name='visitedtasks',
            old_name='visited_level3_clue3',
            new_name='visited_level5_task_clue3',
        ),
        migrations.RenameField(
            model_name='visitedtasks',
            old_name='visited_level3_clue4',
            new_name='visited_level5_task_clue4',
        ),
    ]
