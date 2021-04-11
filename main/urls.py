from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('channels', views.all_channels),
    path('channels/<int:id>', views.channel),
    path('contents', views.all_contents),
    path('contents/<int:id>', views.content),
]
