from django.contrib import admin
from main import views
from django.conf.urls import url, include


urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^courses/', include(('courses.urls', 'courses'), namespace='courses'))
 
]
