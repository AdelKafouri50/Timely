# Generated by Django 3.1.4 on 2021-03-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelyapp', '0019_auto_20210331_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]