# Generated by Django 5.1.2 on 2025-01-31 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_participant_created_at_participant_final_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedquiz',
            name='id',
            field=models.CharField(default='sh67315b22202501312225', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='ue7bc447b202501312225', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
