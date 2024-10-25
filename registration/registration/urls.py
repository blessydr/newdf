
from django.contrib import admin
from django.urls import path,include
from myaccounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
     path('',views.home,name='home' ),
     path('login',views.login,name='login' ),
     path('register',views.register,name='register' ),
     path('index',views.index,name='index' ),
    path('blog_list', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('logout', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)