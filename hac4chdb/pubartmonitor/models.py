from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    deathdate = models.DateField(null=True, blank=True)
    birthCountry = models.CharField(max_length=200, null=True, blank=True)
    deathCountry = models.CharField(max_length=200, null=True, blank=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    opendate = models.DateField(null=True, blank=True)
    closedate = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Location(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)


class Object(models.Model):
    owner = models.CharField(max_length=200, null=True, blank=True)

    #Classification
    cathegory = models.CharField(max_length=200, null=True, blank=True)
    subcathegory = models.CharField(max_length=200, null=True, blank=True)

    #Identification
    denomination = models.CharField(max_length=400, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    #Representation
    iconography = models.TextField(null=True, blank=True)
    iconographyImg = models.ImageField(null=True, blank=True)
    heraldry = models.TextField(null=True, blank=True)
    heraldryImg = models.ImageField(null=True, blank=True)
    inscription = models.TextField(null=True, blank=True)
    inscriptionPt = models.TextField(null=True, blank=True)
    inscriptionEn = models.TextField(null=True, blank=True)

    #Production
    autorship = models.ForeignKey(Author, on_delete=models.CASCADE)
    atributions = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    marks = models.TextField(null=True, blank=True)
    style = models.TextField(null=True, blank=True)

    #Dating
    epoch = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    justification = models.TextField(null=True, blank=True)

    #Technical info
    material_mean = models.CharField(max_length=500, null=True, blank=True)
    material_support = models.CharField(max_length=500, null=True, blank=True)
    technical_structure = models.CharField(max_length=500, null=True, blank=True)
    technical_decoration = models.CharField(max_length=500, null=True, blank=True)

    #Dimensions
    dimensions_height = models.FloatField(null=True, blank=True)
    dimensions_width = models.FloatField(null=True, blank=True)
    dimensions_depth = models.FloatField(null=True, blank=True)
    dimensions_weight = models.FloatField(null=True, blank=True)
    dimensions_other = models.CharField(max_length=500, null=True, blank=True)

    origin = models.CharField(max_length=500, null=True, blank=True)
    incorporation = models.CharField(max_length=500, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class ObjectImage(models.Model):
    img = models.ImageField()
    object = models.ForeignKey(Object, on_delete=models.CASCADE)

class ObjectBibliography(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    bib = models.CharField(max_length=500, null=True, blank=True)

class Exhibition(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    curator = models.CharField(max_length=500, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    objects = models.ManyToManyField(Object)

class Sensor(models.Model):
    serialnumber = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    installationdate = models.DateField(null=True, blank=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    accesskey = models.CharField(max_length=200, null=True, blank=True)

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

class ConservationReport(models.Model):
    conservator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    report = models.TextField(null=True, blank=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)

class SensorStatusReport(models.Model):
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    report = models.TextField(null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
