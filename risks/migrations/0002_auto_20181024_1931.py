# Generated by Django 2.1.2 on 2018-10-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policylist',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]