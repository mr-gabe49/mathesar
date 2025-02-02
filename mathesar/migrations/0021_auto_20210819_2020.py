# Generated by Django 3.1.7 on 2021-08-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0020_merge_20210804_2034'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='schema',
            constraint=models.UniqueConstraint(fields=('oid', 'database'), name='unique_schema'),
        ),
        migrations.AddConstraint(
            model_name='table',
            constraint=models.UniqueConstraint(fields=('oid', 'schema'), name='unique_table'),
        ),
    ]
