# Generated by Django 3.0.3 on 2020-05-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_business_list_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Donor_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donorname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('bloodcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bloodcategory')),
            ],
        ),
    ]
