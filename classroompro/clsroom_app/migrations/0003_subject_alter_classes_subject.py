# Generated by Django 5.0.2 on 2024-04-23 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clsroom_app', '0002_classes_delete_teachermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='classes',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clsroom_app.subject'),
        ),
    ]
