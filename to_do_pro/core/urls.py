from django.urls import path
from .views import TasklistView

urlpatterns = [
    path("",TasklistView.as_view(),name="task-list"),
   
]
