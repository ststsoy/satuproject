# Generated by Django 5.1.1 on 2024-10-05 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesatu', '0005_rename_homesatu_insvid_podcast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insvid',
            name='podcast',
        ),
        migrations.AddField(
            model_name='homesatu',
            name='pcat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homesatu.insvid'),
        ),
    ]
