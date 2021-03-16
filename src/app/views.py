from django.shortcuts import render
from app.models import user_info,tutorial_type,language_type,links_db,suggestion

def home_view(request):
    data_r = tutorial_type.objects.all()  

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
    data_r = links_db.objects.filter(type_value = type_val_info)
    context = { 
               "data_view" : []
               
        }
    print(type_val_info)
    context["data_view"].append({"type_val": type_val_info,"tutor_data":data_r})
    return render(request, "app/tutorials.html",context)