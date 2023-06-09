# Generated by Django 4.1.1 on 2022-10-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='kategoriya nomi', max_length=255)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
