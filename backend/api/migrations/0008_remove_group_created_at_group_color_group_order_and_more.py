# Generated by Django 5.1.2 on 2024-10-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_quiz_quiz_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='created_at',
        ),
        migrations.AddField(
            model_name='group',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='group',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]