# Generated by Django 3.1.2 on 2020-10-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0007_auto_20201015_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_choices', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_choices', models.CharField(max_length=15)),
            ],
        ),
    ]
