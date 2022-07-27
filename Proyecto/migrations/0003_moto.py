# Generated by Django 4.0.6 on 2022-07-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0002_rename_prueba_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('modelo', models.IntegerField()),
                ('fecha_creacion', models.DateField(null=True)),
            ],
        ),
    ]