# Generated by Django 3.0.8 on 2020-08-19 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_link', models.CharField(max_length=500)),
                ('restaurant_content', models.TextField()),
                ('restaurant_keyword', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='shareRes.Category')),
            ],
        ),
    ]
