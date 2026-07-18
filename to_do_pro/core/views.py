from django.shortcuts import render , redirect 
from .models import *
from django.views import View
# Create your views here.

class TasklistView(View):
    def get(self,request):
        tasks = Task.objects.all()

        context = {
            "Tasks":tasks
        }
        return render(request,"core/index.html",context)
    
    def post(self,request):
        name = request.POST.get("name")    
        description = request.POST.get("desc")
        priority = request.POST.get("priority")

        obj = Task.objects.create(name= name,description=description,priority=priority) 
                   
        return redirect("task-list")


