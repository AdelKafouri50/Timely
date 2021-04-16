# Generated by Django 3.2 on 2021-04-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelyapp', '0003_alter_business_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_name',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='currency',
            field=models.CharField(default='USD', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]