# Generated by Django 3.2.7 on 2021-09-05 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_persons_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person_id',
        ),
    ]
