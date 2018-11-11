# Generated by Django 2.1.2 on 2018-11-10 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0006_auto_20181110_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_value', models.CharField(max_length=80)),
                ('field_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risks.Fields')),
            ],
        ),
    ]