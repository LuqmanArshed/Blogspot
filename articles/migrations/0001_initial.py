# Generated by Django 3.1.4 on 2021-03-31 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_date', models.DateField(blank=True, null=True)),
                ('header', models.FloatField(blank=True, null=True)),
                ('category', models.FloatField(blank=True, choices=[('technology', 'technology'), ('sports', 'sports'), ('international', 'international'), ('pakistan', 'pakistan')], null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='BlogImages/')),
                ('details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]