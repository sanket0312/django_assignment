# Generated by Django 2.2.4 on 2022-08-05 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0003_auto_20220805_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='dropship.Member'),
        ),
    ]
