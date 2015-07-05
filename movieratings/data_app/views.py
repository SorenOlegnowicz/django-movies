from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response as rtr
from data_app.models import Movie, Rating, User

# Create your views here.


def home(request):
    context = {}
    return rtr("base.html", context)


def movie_list(request):
    all_movies = Movie.objects.all()
    context = {"titles": all_movies}
    return rtr("movie_list.html", context)


def user_list(request):
    all_users = User.objects.all()
    context = {"users": all_users}
    return rtr("user_list.html", context)


def movie_detail(request, movie_id):
    avglist = []
    try:
        movie = Movie.objects.get(id=movie_id)
        rats = Movie.objects.filter(id=movie_id).values_list('rating__rating')
        for i in rats:
            avglist.append(i[0])
        avgrat = sum(avglist)/len(avglist)
        uovie = User.objects.filter(rating__movie=movie)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"movie": movie, "average": avgrat, "uovie": uovie}
    return rtr("movie_detail.html", context)


def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        muser = Movie.objects.filter(rating__user=user)
        #  ruser = User.objects.filter(rating__)
    except User.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"user": user, "muser": muser}
    return rtr("user_detail.html", context)


def movie_detail_2(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"movie": movie}
    return rtr("movie_detail.html", context)
