from django.conf.urls import url,include
from unifieddbms import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]