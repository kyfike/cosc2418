from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('created/', views.Created, name='created'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

    # Date Table Urls
    path('addDay/', views.addDay, name='addDay'),
    path('addDay/addrecordDay/', views.addrecordDay, name='addrecordDay'),
    path('deleteDay/<int:id>', views.deleteDay, name='deleteDay'),
    path('updateDay/<int:id>', views.updateDay, name='updateDay'),
    path('updateDay/updaterecordDay/<int:id>', views.updaterecordDay, name='updaterecordDay'),
]