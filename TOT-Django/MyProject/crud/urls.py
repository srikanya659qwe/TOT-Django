from django.urls import path
from crud import views
urlpatterns = [
    path('addstudent/',views.addstudent,name='add'),
    path('display/',views.display,name='display'),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<str:name>',views.delete,name='delete'),



]
