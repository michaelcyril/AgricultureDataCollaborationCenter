# Generated by Django 3.2.15 on 2022-09-22 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainInformations', '0002_rename_soil_id_productimage_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Des',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='desease',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainInformations.des'),
        ),
    ]