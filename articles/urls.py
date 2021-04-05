from django.urls import path
from django.conf import settings

from django.conf.urls.static import static


from . import views 

urlpatterns = [
     path('', views.home, name='home'),
     path('user_home', views.user_home, name='user_home'),
     path('login/', views.login_page, name='login_page'),
	path('logout/', views.logoutuser, name='logoutuser'),
     path('newblog', views.new_blog, name='newblog'),
     path('editblog/<int:id>/', views.edit_blog, name='editblog'),
     path('blog/<int:id>/', views.blog_view, name='viewblog'),
    
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)