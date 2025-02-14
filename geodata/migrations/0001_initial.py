# Generated by Django 3.1.4 on 2023-05-10 09:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoJsonUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='geojson')),
            ],
        ),
        migrations.CreateModel(
            name='GeoRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('properties', models.JSONField()),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodata.geojsonupload')),
            ],
        ),
    ]
