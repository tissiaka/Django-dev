# Generated by Django 4.0 on 2021-12-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('https', models.BooleanField(default=False)),
            ],
        ),
    ]
