# Generated by Django 5.1.2 on 2024-12-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_user_account_remove_user_is_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_connected',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]
