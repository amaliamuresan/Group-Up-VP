# Generated by Django 3.1.2 on 2020-10-15 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0008_postdomain_posttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdomain',
            old_name='domain_choices',
            new_name='choices',
        ),
        migrations.RenameField(
            model_name='posttype',
            old_name='type_choices',
            new_name='choices',
        ),
    ]
