# Generated by Django 4.0.5 on 2022-06-13 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('deathdate', models.DateField(blank=True, null=True)),
                ('birthCountry', models.CharField(blank=True, max_length=200, null=True)),
                ('deathCountry', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('opendate', models.DateField(blank=True, null=True)),
                ('closedate', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=200, null=True)),
                ('cathegory', models.CharField(blank=True, max_length=200, null=True)),
                ('subcathegory', models.CharField(blank=True, max_length=200, null=True)),
                ('denomination', models.CharField(blank=True, max_length=400, null=True)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('iconography', models.TextField(blank=True, null=True)),
                ('iconographyImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('heraldry', models.TextField(blank=True, null=True)),
                ('heraldryImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('inscription', models.TextField(blank=True, null=True)),
                ('inscriptionPt', models.TextField(blank=True, null=True)),
                ('inscriptionEn', models.TextField(blank=True, null=True)),
                ('atributions', models.TextField(blank=True, null=True)),
                ('marks', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('epoch', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('justification', models.TextField(blank=True, null=True)),
                ('material_mean', models.CharField(blank=True, max_length=500, null=True)),
                ('material_support', models.CharField(blank=True, max_length=500, null=True)),
                ('technical_structure', models.CharField(blank=True, max_length=500, null=True)),
                ('technical_decoration', models.CharField(blank=True, max_length=500, null=True)),
                ('dimensions_height', models.FloatField(blank=True, null=True)),
                ('dimensions_width', models.FloatField(blank=True, null=True)),
                ('dimensions_depth', models.FloatField(blank=True, null=True)),
                ('dimensions_weight', models.FloatField(blank=True, null=True)),
                ('dimensions_other', models.CharField(blank=True, max_length=500, null=True)),
                ('origin', models.CharField(blank=True, max_length=500, null=True)),
                ('incorporation', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('autorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.author')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.location')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialnumber', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('installationdate', models.DateField(blank=True, null=True)),
                ('accesskey', models.CharField(blank=True, max_length=200, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.object')),
            ],
        ),
        migrations.CreateModel(
            name='SensorStatusReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('report', models.TextField(blank=True, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.sensor')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.object')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectBibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bib', models.CharField(blank=True, max_length=500, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.object')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('curator', models.CharField(blank=True, max_length=500, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.location')),
                ('objects', models.ManyToManyField(to='pubartmonitor.object')),
            ],
        ),
        migrations.CreateModel(
            name='ConservationReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('report', models.TextField(blank=True, null=True)),
                ('conservator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pubartmonitor.object')),
            ],
        ),
    ]
