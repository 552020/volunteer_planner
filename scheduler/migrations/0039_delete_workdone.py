# Generated by Django 2.2.3 on 2022-03-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0038_protect_deletion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WorkDone',
        ),
    ]
