# Generated by Django 4.2.5 on 2024-04-16 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('age_limit', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('photo', models.ImageField(default='performances_photos/default.jpg', upload_to='performances_photos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', to_field='name')),
            ],
        ),
    ]
