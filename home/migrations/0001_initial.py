# Generated by Django 5.1 on 2024-09-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('business_types', models.CharField(max_length=100)),
                ('advertise', models.CharField(max_length=100)),
                ('budget', models.IntegerField(default=0)),
                ('message', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('advertise_count', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
    ]