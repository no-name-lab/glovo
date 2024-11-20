from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user-list')
router.register(r'stores', StoreViewSet, basename='store-list')
router.register(r'products', ProductViewSet, basename='product-list')
router.register(r'orders', UserViewSet, basename='order-list')
router.register(r'couriers', CourierViewSet, basename='courier-list')
router.register(r'reviews', ReviewViewSet, basename='review-list')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

