# Generated by Django 3.0.2 on 2020-05-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
