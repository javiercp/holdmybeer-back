# Generated by Django 2.0.6 on 2018-06-29 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chigre', '0016_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pub',
            name='singleton_enforce',
        ),
    ]
