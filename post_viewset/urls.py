from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

#1 chi uslib
# urlpatterns = [
#
#     ] + router.urls

#2 chi uslub
# urlpatterns = [
#
# ]
# urlpatterns += router.urls

#3 chi uslub
urlpatterns = [
    path('router/', include(router.urls))
]