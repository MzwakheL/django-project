# Generated by Django 4.2 on 2023-04-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_name_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
