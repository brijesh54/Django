# Generated by Django 3.1.2 on 2020-12-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='image',
            field=models.ImageField(upload_to='Picturs/'),
        ),
    ]
