# Generated by Django 5.1.2 on 2025-02-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_sharedquiz_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedquiz',
            name='id',
            field=models.CharField(default='sh0debb494202502010445', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='u18dc6efe202502010445', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
