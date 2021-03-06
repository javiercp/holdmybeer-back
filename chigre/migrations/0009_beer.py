# Generated by Django 2.0.4 on 2018-06-09 15:44

import chigre.models.common
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chigre', '0008_auto_20180608_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('abv', models.DecimalField(decimal_places=2, max_digits=5)),
                ('webpage', models.CharField(blank=True, default='', max_length=100)),
                ('logo', models.CharField(blank=True, default='', max_length=100)),
                ('beertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chigre.BeerType')),
                ('brewery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chigre.Brewery')),
                ('creator', models.ForeignKey(on_delete=models.SET(chigre.models.common.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
