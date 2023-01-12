from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, CreateRating


router = DefaultRouter()
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rating/', CreateRating.as_view()),     
]