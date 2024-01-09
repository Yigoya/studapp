# Generated by Django 5.0 on 2024-01-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_classroompost_isseen'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField()),
                ('name', models.TextField()),
                ('idname', models.TextField(unique=True)),
                ('avatar', models.ImageField(upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]