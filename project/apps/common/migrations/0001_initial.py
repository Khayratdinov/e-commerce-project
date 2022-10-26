# Generated by Django 4.1.2 on 2022-10-25 14:43

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('description_contact', models.TextField(blank=True)),
                ('description_footer', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('telegram', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeadImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Available'), ('False', 'Not Available')], default='True', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('shape', models.ImageField(blank=True, upload_to='images/')),
                ('cover', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Published'), ('False', 'Not Published')], default='True', max_length=15)),
                ('url', models.CharField(blank=True, max_length=555)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
