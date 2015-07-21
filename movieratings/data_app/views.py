from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response as rtr
from django.template import RequestContext

from data_app.models import Movie, Rating, User
from data_app.forms import RatingForm
# Create your views here.


def home(request):
    context = {}
    return rtr("base.html", context, context_instance=RequestContext(request))


def movie_list(request):
    all_movies = Movie.objects.all()
    context = {"titles": all_movies}
    return rtr("movie_list.html", context, context_instance=RequestContext(request))


def user_list(request):
    all_users = User.objects.all()
    context = {"users": all_users}
    return rtr("user_list.html", context, context_instance=RequestContext(request))


@login_required
def movie_detail(request, movie_id):
    avglist = []
    try:
        movie = Movie.objects.get(id=movie_id)
        rats = Movie.objects.filter(id=movie_id).values_list('rating__rating', flat=True)
        avgrat = sum(rats)/len(rats)
        uovie = User.objects.filter(rating__movie=movie)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"movie": movie, "average": avgrat, "uovie": uovie}
    return rtr("movie_detail.html", context, context_instance=RequestContext(request))


@login_required
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        muser = Movie.objects.filter(rating__user=user)
    except User.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"user": user, "muser": muser}
    #  I don't quite understand this code yet.
    """if request.user == user.rater:
        if request.POST:
            rating_instance = Rating(user=user)
            form = RatingForm(request.POST, instance=rating_instance)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse("splat_list"))"""
    return rtr("user_detail.html", context, context_instance=RequestContext(request))


def movie_detail_2(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"movie": movie}
    return rtr("movie_detail.html", context, context_instance=RequestContext(request))


def registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("home")
        except ValueError:
            return rtr("registration/create_user.html",
                       {'form': user_form},
                       context_instance=RequestContext(request))
    return rtr("registration/create_user.html",
               {'form': UserCreationForm()},
               context_instance=RequestContext(request))
