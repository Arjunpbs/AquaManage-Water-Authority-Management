# Generated by Django 4.2.5 on 2023-12-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reader_visit_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
