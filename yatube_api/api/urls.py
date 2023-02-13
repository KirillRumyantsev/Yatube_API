from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet),
router_v1.register('groups', GroupViewSet),
router_v1.register(r'follow', FollowViewSet, basename='Follow'),
router_v1.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
