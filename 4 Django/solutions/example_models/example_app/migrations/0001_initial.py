# Generated by Django 3.0.5 on 2020-04-22 19:32

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
                ('first_name', models.TextField(default='first')),
                ('last_name', models.TextField(default='first')),
                ('age', models.IntegerField(default=0)),
                ('favorite_pet', models.TextField(blank=True, default='first', null=True)),
            ],
        ),
    ]