from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post_app.views import PostViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
