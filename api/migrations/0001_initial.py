# Generated by Django 3.2.9 on 2021-11-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=50, unique=True)),
                ('keyword', models.CharField(max_length=20)),
                ('engine', models.CharField(max_length=20)),
                ('context', models.TextField(max_length=5000)),
                ('link_title', models.CharField(max_length=100)),
                ('abs_context', models.TextField()),
                ('recommendation', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField()),
                ('URL', models.CharField(max_length=50)),
                ('web_kind', models.CharField(max_length=20)),
                ('pro_con', models.BooleanField(default=1)),
            ],
        ),
    ]
