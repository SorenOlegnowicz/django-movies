from django.db import models


class Movie(models.Model):
    m_id = models.IntegerField(default=None)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    @property
    def genre_list(self):
        return self.genres.split('|')


class Rating(models.Model):
    user = models.ForeignKey('User')
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=None)
    timestamp = models.BigIntegerField(default=None)

    def __str__(self):
        return 'User: {}, Rating: {}'.format(self.user, str(self.rating))

class User(models.Model):
    user_id = models.IntegerField(default=None)
    gender = models.CharField(max_length=1)
    age = models.IntegerField(default=None)
    occupation = models.IntegerField(default=None)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)
