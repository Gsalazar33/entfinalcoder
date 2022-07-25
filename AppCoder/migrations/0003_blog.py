# Generated by Django 4.0.2 on 2022-07-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('contenido', models.CharField(max_length=1000)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='blog')),
            ],
        ),
    ]