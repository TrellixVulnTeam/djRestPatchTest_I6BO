# Generated by Django 3.1.2 on 2020-10-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
