# Generated by Django 5.0 on 2024-01-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_groupchat_groupuser_delete_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='avatar',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]