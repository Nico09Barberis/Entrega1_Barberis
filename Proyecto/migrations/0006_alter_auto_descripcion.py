# Generated by Django 4.0.6 on 2022-08-01 22:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0005_auto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]