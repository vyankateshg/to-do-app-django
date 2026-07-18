from django.shortcuts import render , redirect
from .models import *
from django.views import View
# Create your views here.

class TasklistView(View):
    def get_task(self,request):
        tasks = Task.objects.all()

        context = {
            "Tasks":tasks
        }
        return render(request,"core/index.html",context)