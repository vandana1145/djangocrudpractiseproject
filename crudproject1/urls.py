from django.contrib import admin
from django.urls import path
from crudapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name='addandshow'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('update/<int:id>/', views.update_data, name='updatedata')
]
