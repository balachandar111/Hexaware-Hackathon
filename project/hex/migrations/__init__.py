# Generated by Django 5.0.7 on 2024-08-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Email',models.CharField(default='',max_length=20)),
                
                ('Address', models.CharField(default='', max_length=20)),
                
                ('Password', models.CharField(default='', max_length=20)),
                ('Cpassword', models.CharField(default='', max_length=20))
                
            ],
        ),
    ]
