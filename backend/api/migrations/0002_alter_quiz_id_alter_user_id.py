# Generated by Django 5.1.2 on 2025-01-19 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.CharField(default='q1259519e5b84207b392d594b14c31dc', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='uee415c609d142938c590b5aa815f2cb', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
