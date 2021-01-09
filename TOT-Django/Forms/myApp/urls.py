from django.urls import path
from myApp import views
urlpatterns = [
	path('dynamic/',views.dynamic,name='dynamic'),
	#path('details/',views.details,name='details'),
	path('register/',views.registerForm,name='register'),
	path('fetch/',views.fetch,name='fetch'),
	path('nav/',views.nav,name='nav'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('delete/<int:id>',views.delete,name='delete'),
    
]

