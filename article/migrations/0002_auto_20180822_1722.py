# Generated by Django 2.0.7 on 2018-08-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]