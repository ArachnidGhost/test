# Generated by Django 5.1.3 on 2024-12-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.AddField(
            model_name='registration',
            name='available_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='user_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]