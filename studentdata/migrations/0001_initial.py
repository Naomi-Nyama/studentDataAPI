# Generated by Django 4.2.5 on 2023-10-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('dateOfBirth', models.DateField()),
                ('email', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
            ],
        ),
    ]
