# Generated by Django 3.1.3 on 2020-11-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(choices=[('remote', '1'), ('office', '2')], default='office', max_length=10)),
                ('posted_on', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
