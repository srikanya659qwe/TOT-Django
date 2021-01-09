from django.urls import path
from newApp import views
urlpatterns = [
	path('dynamic/',views.dynamic,name='dynamic'),
	#path('details/',views.details,name='details'),
	
    
]

