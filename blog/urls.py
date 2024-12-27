from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('kategori/<slug:slug>/', views.category_list, name='category_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', 
         views.post_detail, 
         name='post_detail'),
] 