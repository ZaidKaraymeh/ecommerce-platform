from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from users.models import CustomUser
from .models import Shop, Product, ProductOrder, UserRating
from api.serializers import ShopSerializer, ProductSerializer, UserRatingSerializer, UserSerializer
from rest_framework import permissions, authentication

from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    permission_classes_by_action = {
        'create': [permissions.AllowAny],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'destroy': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'retrieve': [permissions.IsAuthenticatedOrReadOnly],
        'update': [permissions.IsAdminUser, permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["list"]
            ]

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
    permission_classes_by_action = {
        'create': [permissions.IsAdminUser],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'destroy': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'retrieve': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser, permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["list"]
            ]

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        # assuming your author class has foreign key to user
        if current_user or self.action == "list":
            shops = Shop.objects.all()
        else:
            shops = Shop.objects.filter(owner=current_user)

        return shops

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes_by_action = {
        'create': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'destroy': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'retrieve': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser, permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["list"]
            ]

class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes_by_action = {
        'create': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'list': [permissions.IsAuthenticated],
        'destroy': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'retrieve': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser, permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["list"]
            ]

