# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0007_add_validate_permission_on_xform'),
    ]

    operations = [
        migrations.AddField(
            model_name='xform',
            name='allow_auth_submit',
            field=models.BooleanField(default=False),
        ),
    ]