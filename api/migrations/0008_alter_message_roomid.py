# Generated by Django 5.0 on 2023-12-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_message_created_alter_student_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='roomid',
            field=models.CharField(max_length=250),
        ),
    ]