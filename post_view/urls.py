from django.urls import path
from .views import PostListView, \
    PostCreateView, \
    PostRetrieveView, \
    PostUpdateView, \
    PostPartialView, PostDeleteView, PostListCreateView,\
    PostRUDView

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('detail/<int:pk>/', PostRetrieveView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('update/<int:pk>/', PostUpdateView.as_view()),
    path('update/partial/<int:pk>/', PostPartialView.as_view()),
    path('delete/<int:pk>/', PostDeleteView.as_view()),
    path('list-create/', PostListCreateView.as_view()),
    path('rud/<int:pk>/', PostRUDView.as_view()),
]
