# Generated by Django 5.1.5 on 2025-02-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.CharField(choices=[('Trabalho', 'Trabalho'), ('Pessoal', 'Pessoal'), ('Estudo', 'Estudo'), ('Outro', 'Outro')], default='Outro', max_length=15),
        ),
    ]
