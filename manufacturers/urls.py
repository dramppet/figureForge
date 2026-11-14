from django.urls import path,include
from . import views
app_name='manufacturers'
urlpatterns=[
    path('',views.ItemList.as_view(),name='list'),
    path('add/',views.ItemCreate.as_view(),name='add'),
    path('<int:pk>/',include([
        path('',views.ItemDetail.as_view(),name='detail'),
        path('update/',views.ItemUpdate.as_view(),name='update'),
        path('delete/',views.ItemDelete.as_view(),name='delete'),
    ])),
]