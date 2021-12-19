# Generated by Django 3.0.8 on 2020-08-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='funding_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('stage', models.CharField(choices=[(1, 'Idea'), (2, 'Concept'), (3, 'Established')], default=1, max_length=30)),
                ('problem', models.TextField(max_length=500)),
                ('solution', models.TextField(max_length=500)),
                ('company', models.CharField(choices=[(1, 'Yes'), (2, 'No')], default=2, max_length=30)),
            ],
        ),
    ]
