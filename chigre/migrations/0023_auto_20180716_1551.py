# Generated by Django 2.0.7 on 2018-07-16 15:51

import chigre.models.common
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chigre', '0022_auto_20180716_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='updater',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(chigre.models.common.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
