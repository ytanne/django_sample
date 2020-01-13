from django.shortcuts import (
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

import json
from .models import Car

def list_cars(request):
    cars = Car.objects.all()
    all_cars = {}
    for car in cars:
        all_cars.update({car.manufacturer: model_to_dict(car)})
    return (JsonResponse(all_cars, safe=False))

def create_dict(request):
    features = json.loads(request.body)
    return (features)

def get_feature(features, feature):
    if (feature in features):
        return (features[feature])
    else:
        return (None)

def create_car(request):
    features = create_dict(request)
    manufacturer = get_feature(features, "manufacturer")
    colour = get_feature(features, "colour")
    year = get_feature(features, "year")
    if (manufacturer and colour):
        new_car = Car(manufacturer=manufacturer, colour=colour)
        if (year):
            new_car.year = year
        new_car.save()
    return (list_cars(request))

def update_car(features, car_instance):
    manufacturer = get_feature(features, "manufacturer")
    colour = get_feature(features, "colour")
    year = get_feature(features, "year")
    if (manufacturer):
        car_instance.manufacturer = manufacturer
    if (colour):
        car_instance.colour = colour
    if (year):
        car_instance.year = year
    car_instance.save()

@csrf_exempt
def create_or_list(request):
    if (request.method == "POST"):
        return (create_car(request))
    elif (request.method == "GET"):
        return (list_cars(request))
    else:
        return (HttpResponse("<h1>Page was found</h1>"))

@csrf_exempt
def manipulate_by_id(request, car_id):
    car_instance = get_object_or_404(Car, id=car_id)
    car_json = model_to_dict(car_instance)
    if (request.method == "GET"):
        return (JsonResponse(car_json, safe=False))
    if (request.method == "DELETE"):
        car_instance.delete()
        return (list_cars(request))
    if (request.method == "PATCH"):
        features = create_dict(request)
        update_car(features, car_instance)
        return (list_cars(request))
    else:
        return (HttpResponse("<h1>Method was not found</h1>"))

