# Generated by Django 5.1.2 on 2025-01-31 21:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_sharedquiz_id_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='final_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='password',
            field=models.CharField(default='test123', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='participant',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='api.quiz'),
        ),
        migrations.AlterField(
            model_name='sharedquiz',
            name='id',
            field=models.CharField(default='sh926b85a0202501312101', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='u7512e3d4202501312101', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
