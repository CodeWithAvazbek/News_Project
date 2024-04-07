from django.urls import path
from .views import news_list, detail, index, contact, page_404

urlpatterns = [
    path('', index, name='index'),
    path('lists/', news_list, name='news_list'),
    path('detail/<int:news_id>/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('page_404/', page_404, name='404')
]
