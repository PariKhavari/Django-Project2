from django.http import Http404, JsonResponse
from django.shortcuts import render
import json

# Create your views here.


def send_fruits(request):

    fruits = [
        {"name": "Apfel",  "weight": 200, "color": "red",
            "image": "apfel.jpg", "is_ordered": True},
        {"name": "Banane", "weight": 120, "color": "yellow",
            "image": "banane.jpg", "is_ordered": False},
        {"name": "Birne", "weight": 5, "color": "purple",
            "image": "birne.jpg", "is_ordered": False},
        {"name": "Kirsche",   "weight": 220, "color": "green",
            "image": "kirsche.jpg", "is_ordered": True},
        {"name": "Orange", "weight": 250, "color": "orange",
            "image": "orange.jpg", "is_ordered": True},
    ]

    if request.method == "GET":
        return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})
        return JsonResponse(fruits, safe=False)

    raise Http404("fruit not found")


def info_fruits(request):
    return render(request, "fruit_app/info.html")
# name der Obst soll dahinten der html kommen
