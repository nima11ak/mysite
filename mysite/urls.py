
from django.contrib import admin
from django.urls import path
from .views import Http_test,json_test 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Http-test',Http_test),
    path('json-test', json_test)

]
