# Generated by Django 2.0.7 on 2018-09-24 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20180913_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Board',
            new_name='board',
        ),
    ]