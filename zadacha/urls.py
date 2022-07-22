"""zadacha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from task1 import views
from task1.views import ZadachaCreate
from task1.views import ZadachaListView
from task1.views import ZadachaDetails, ZadachaUpdate, ZadachaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("task_create/", ZadachaCreate.as_view()),
    path("task_list/", ZadachaListView.as_view()),
    path("task_detail/<pk>/", ZadachaDetails.as_view()),
    path("task_update/<pk>/", ZadachaUpdate.as_view()),
    path("task_delete/<pk>/", ZadachaDelete.as_view()),
]
