from django.urls import path
from django.urls import path
from app import views
app_name='app'

urlpatterns = [
    path('sample1/',views.sample1,name="sample1"),
    path('sample2/',views.sample2,name="sample2"),
]
