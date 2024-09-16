# Generated by Django 5.1 on 2024-09-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertise',
            old_name='business_types',
            new_name='business_type',
        ),
        migrations.RemoveField(
            model_name='advertise',
            name='advertise_count',
        ),
        migrations.RemoveField(
            model_name='advertise',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='advertise',
            name='advertise',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='budget',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]