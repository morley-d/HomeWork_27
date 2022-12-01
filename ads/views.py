from django.shortcuts import render
from ads.models import Ads, Category


def index(request):
    return 200, {"status": "ok"}
