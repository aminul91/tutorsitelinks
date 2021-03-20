from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import requests
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import *
from app.models import *

def home_view(request):
    data_r = tutorial_types.objects.all()  

    context = { 
	"shumon" : []

	}


    context["shumon"].append({"tutorial":data_r})

    return render(request, "app/home.html",context)
    
def tutor_topic(request):
    data_r=""
    type_val_info=0
    if request.method == "POST":
        type_val_info = request.POST.get('type_val')
        type_val_info = int(type_val_info)
    data_r = tutorials_paths.objects.filter(type_value = type_val_info)
    context = { 
               "data_view" : []
               
        }
    print(type_val_info)
    context["data_view"].append({"type_val": type_val_info,"tutor_data":data_r})
    return render(request, "app/tutorials.html",context)

@api_view(['GET'])
def tutorials_links(request):
    data_r = tutorials_paths.objects.all()
    serial_data = linksSerializer(data_r,many = True)
    return Response(serial_data.data)

def api_links(request):
    response_links= requests.get("https://tutorsitelinks.herokuapp.com/tutorials/").json()
    context = { 
               "data_view" : []
               
        }
    context["data_view"].append({"response": response_links})
    return render(request, "app/api_links.html",context)

@api_view(['GET'])
def values(request,username):
    print(username)
    username=str(username)
    data_r = language_type.objects.filter(language_name=username)
    print("pp")
    for req in data_r:
        print(req.language_name)
        num=int(req.language_value)
    links_r = tutorials_paths.objects.filter(language_value=num)
    serial_data = linksSerializer(links_r,many = True)
    return Response(serial_data.data)

def values_double(request,language,tutorial):
    print(language)
    print(tutorial)
    context = { 
               "data_view" : []
               
        }
    context["data_view"].append({"language": language,"tutorial": tutorial})
    return render(request, "app/message.html",context)
