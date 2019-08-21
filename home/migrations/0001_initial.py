# Generated by Django 2.0.1 on 2019-08-18 20:55

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=250, null=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('thumbnail', models.CharField(default=None, max_length=120)),
                ('tech', models.CharField(default=None, max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]