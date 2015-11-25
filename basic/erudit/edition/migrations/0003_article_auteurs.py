# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edition', '0002_auto_20151125_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auteurs',
            field=models.ManyToManyField(to='edition.Auteur'),
        ),
    ]
