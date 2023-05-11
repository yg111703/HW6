# Generated by Django 4.2.1 on 2023-05-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('percent', models.FloatField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
    ]
