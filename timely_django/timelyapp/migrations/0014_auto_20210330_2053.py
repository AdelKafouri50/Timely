# Generated by Django 3.1.4 on 2021-03-31 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelyapp', '0013_auto_20210330_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='purchase_order',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timelyapp.invoice'),
        ),
    ]
