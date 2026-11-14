from django.urls import path,include
from . import views

app_name='user'
urlpatterns=[
    path('',views.ItemList.as_view(),name='list'),
    path('add/',views.ItemCreate.as_view(),name='add'),
    path('<int:pk>/',include([
     path('',views.ItemDetail.as_view(),name='detail'),
    path('<int:pk>/edit/',views.ItemUpdate.as_view(),name='edit'),
    path('<int:pk>/delete/',views.ItemDelete.as_view(),name='delete')]))
]
