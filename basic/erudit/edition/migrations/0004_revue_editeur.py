# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edition', '0003_article_auteurs'),
    ]

    operations = [
        migrations.AddField(
            model_name='revue',
            name='editeur',
            field=models.ForeignKey(null=True, to='edition.Editeur', blank=True),
        ),
    ]
