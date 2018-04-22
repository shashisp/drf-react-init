# Generated by Django 2.0.4 on 2018-04-22 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180415_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expert',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]