# Generated by Django 3.2 on 2021-04-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hood',
            field=models.CharField(max_length=200),
        ),
    ]
