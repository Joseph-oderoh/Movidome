# Generated by Django 4.0.4 on 2022-06-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0003_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='', verbose_name='pictures'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='pictures/'),
        ),
    ]