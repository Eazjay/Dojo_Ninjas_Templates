# Generated by Django 2.2.4 on 2021-03-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
