# Generated by Django 4.2.5 on 2023-10-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0002_remove_student_dateofbirth_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=225)),
            ],
        ),
    ]