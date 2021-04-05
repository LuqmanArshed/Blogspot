# Generated by Django 3.1.4 on 2021-03-31 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210331_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='center_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_image',
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='BlogImages/')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='BlogImages/')),
                ('center_image', models.ImageField(blank=True, null=True, upload_to='BlogImages/')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.blog')),
            ],
        ),
    ]
