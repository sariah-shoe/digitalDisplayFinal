# Generated by Django 5.0 on 2024-02-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_employee_working_alter_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='color',
            field=models.CharField(default='255, 200, 25', max_length=50),
        ),
    ]
