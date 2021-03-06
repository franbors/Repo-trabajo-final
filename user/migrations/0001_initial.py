# Generated by Django 4.0.5 on 2022-06-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('SU', 'Super_user'), ('RU', 'Regular_user')], max_length=2)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('last_login', models.DateField()),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
