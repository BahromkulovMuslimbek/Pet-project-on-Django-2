# Generated by Django 5.0.7 on 2024-07-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurStudentsSay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.TextField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
