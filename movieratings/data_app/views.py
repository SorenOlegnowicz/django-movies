from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response as rtr
from data_app.models import Movie, Rating, User

# Create your views here.

def movie_list(request):
    all_movies = Movie.objects.all()
    context = {"title": all_movies}
    return rtr("movie_list.html", context)


def user_list(request):
    all_users = User.objects.all()
    context = {"users": all_users}
    return rtr("user_list.html", context)


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"movie": movie}
    return rtr("movie_detail.html", context)


def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"user": user}
    return rtr("user_detail.html", context)



"""def splat_detail(request, splat_id):
    try:
        splat = Splat.objects.get(id=splat_id)
    except Splat.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"splat": splat}
    return render_to_response("splat_detail.html", context)


def user_detail(request, user_id):
    try:
        splatee = Splatee.objects.get(id=user_id)
    except Splatee.DoesNotExist:
        return HttpResponseNotFound("Not Found!")
    context = {"splatee": splatee}
    return render_to_response("user_detail.html", context)"""
