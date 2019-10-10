# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    bio = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'author'


class Quotes(models.Model):
    content = models.CharField(max_length=1500)
    tags = models.CharField(max_length=150)
    author = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quotes'


class Tags(models.Model):
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'
