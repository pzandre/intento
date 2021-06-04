# Generated by Django 3.2.3 on 2021-06-03 22:38

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='base_text',
            new_name='base_text_1',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='bibliographic_reference',
            new_name='bibliographic_reference_1',
        ),
        migrations.AddField(
            model_name='question',
            name='base_text_2',
            field=django_quill.fields.QuillField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='base_text_3',
            field=django_quill.fields.QuillField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='bibliographic_reference_2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='bibliographic_reference_3',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
