# Generated by Django 3.2.7 on 2021-09-22 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 17, 6, 51, 259026), verbose_name='fecha de publicacion'),
        ),
    ]
