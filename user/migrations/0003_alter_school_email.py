# Generated by Django 4.1.7 on 2023-03-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_school_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
