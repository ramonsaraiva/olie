# Generated by Django 3.0.3 on 2020-05-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200501_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
