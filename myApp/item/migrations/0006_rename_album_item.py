# Generated by Django 4.2 on 2023-04-24 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_album_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='album',
            new_name='Item',
        ),
    ]