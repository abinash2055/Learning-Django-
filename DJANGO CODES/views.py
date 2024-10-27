from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from profiles.models import Profile

# Create your views here.


def soft_delete_profile(request, pk):
    if not request.user.is_superuser:
        raise Http404("YOU ARE NOT ALLOWED")

    profile = Profile.objects.get(id=pk)
    profile.deleted = True
    profile.save()
    return redirect(request.META.get("HTTP_REFERER"))


def recover_profile(request, pk):
    if not request.user.is_superuser:
        raise Http404("YOU ARE NOT ALLOWED")

    profile = Profile.objects.get(id=pk)
    profile.deleted = False
    profile.save()
    return redirect(request.META.get("HTTP_REFERER"))


def hard_delete_profile(request, pk):
    if not request.user.is_superuser:
        raise Http404("YOU ARE NOT ALLOWED")

    profile = Profile.objects.get(id=pk)
    profile.delete()
    return redirect(request.META.get("HTTP_REFERER"))


# DONT REDIRECT TO A URL LIKE THIS...
