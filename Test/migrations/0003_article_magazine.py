# Generated by Django 3.2 on 2021-05-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_magazine'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ManyToManyField(to='Test.Magazine'),
        ),
    ]