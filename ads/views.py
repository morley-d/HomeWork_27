from django.shortcuts import render


def index(request):
    return 200, {"status": "ok"}
