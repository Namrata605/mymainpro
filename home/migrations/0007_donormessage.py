# Generated by Django 3.0.3 on 2020-05-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bloodcategory_donor_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(max_length=100)),
                ('email2', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
