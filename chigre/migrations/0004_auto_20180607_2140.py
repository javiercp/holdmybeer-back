# Generated by Django 2.0.4 on 2018-06-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chigre', '0003_kegtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegtype',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
