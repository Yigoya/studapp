# Generated by Django 3.2.21 on 2023-12-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_entrancequestion_explain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='graderange',
            field=models.CharField(max_length=20, null=True),
        ),
    ]