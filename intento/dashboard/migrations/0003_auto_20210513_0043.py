# Generated by Django 3.2.2 on 2021-05-13 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210507_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='revision_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.question', verbose_name='answer'),
        ),
    ]
