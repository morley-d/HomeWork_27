import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ads, Category


def index(request):
    return HttpResponse({"status": "ok"})


@csrf_exempt
def ads(request):
    if request.method == "GET":
        ad_list = Ads.objects.all()
        response = []
        for ad in ad_list:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
    elif request.method == "POST":
        ad_data = json.loads(request.body)
        ad = Ads()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]
        ad.save()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


def get_ad(request, pk):
    try:
        ad = Ads.objects.get(id=pk)
    except Ads.DoesNotExist:
        return JsonResponse({"error": "Ad not found"}, status=404)
    return JsonResponse({
        "id": ad.id,
        "name": ad.name,
        "author": ad.author,
        "price": ad.price,
        "description": ad.description,
        "address": ad.address,
        "is_published": ad.is_published,
    },
        json_dumps_params={"ensure_ascii": False}
    )


@csrf_exempt
def cats(request):
    if request.method == "GET":
        cats_list = Category.objects.all()
        response = []
        for cat in cats_list:
            response.append({
                "id": cat.id,
                "name": cat.name,
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
    elif request.method == "POST":
        cat_data = json.loads(request.body)
        cat = Category()
        cat.name = cat_data["name"]
        cat.save()
        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })


def get_cat(request, pk):
    try:
        cat = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Cat not found"}, status=404)
    return JsonResponse({
        "id": cat.id,
        "name": cat.name,
    },
    json_dumps_params={"ensure_ascii": False}
    )
