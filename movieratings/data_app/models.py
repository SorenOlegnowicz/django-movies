from django.db import models

# Create your models here.
class Movies(models.Model):
    m_id = models.IntegerField()
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)


class Ratings(models.Model):
    user_id = models.IntegerField()
    m_id = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()


class User(models.Model):
    user_id = models.IntegerField()
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zipcode = models.IntegerField()
