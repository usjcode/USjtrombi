# Generated by Django 4.1.4 on 2023-01-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trombinoscope', '0005_member_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(default='default.jpeg', upload_to=''),
        ),
    ]