# Generated by Django 4.1.4 on 2023-01-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trombinoscope', '0006_alter_member_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
