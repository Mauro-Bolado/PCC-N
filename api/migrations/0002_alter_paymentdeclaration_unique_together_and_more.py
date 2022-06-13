# Generated by Django 4.0.4 on 2022-06-12 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paymentdeclaration',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='militant',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 23, 14, 34, 725177)),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('street', 'municipality', 'province', 'neighborhood', 'corner_or_ave', 'apto')},
        ),
    ]
