from django.urls import path
from .views import news_list, detail, index

urlpatterns = [
    path('', index, name='index'),
    path('lists/', news_list, name='news_list'),
    path('detail/<int:news_id>/', detail, name='detail')
]
