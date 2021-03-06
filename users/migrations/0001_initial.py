# Generated by Django 3.0.8 on 2020-07-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
