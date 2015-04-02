# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QAforum', '0002_auto_20150316_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('question_id', models.ForeignKey(to='QAforum.Question', to_field='id')),
                ('answer_text', models.CharField(max_length=500)),
                ('is_anonymous', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
