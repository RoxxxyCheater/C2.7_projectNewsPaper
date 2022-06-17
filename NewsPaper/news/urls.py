from django.urls import path
from .views import PostList, PostDetail, Posts
from django.urls import path
from .views import PostList, PostDetail, Posts, PostAdd, PostDeleteView, PostUpdateView
 
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', Posts.as_view(), name='search'),
    path('add_news/', PostAdd.as_view(), name='post_create'),
    path('<int:pk>/post_delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/post_update/', PostUpdateView.as_view(), name='post_update'),
    
]