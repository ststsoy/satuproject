# Generated by Django 5.1.1 on 2024-10-05 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homesatu', '0002_insvid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insvid',
            old_name='insvid',
            new_name='podcast',
        ),
    ]
