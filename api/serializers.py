from rest_framework import serializers
from .models import Shop, Product, ProductOrder, UserRating
from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRating
        fields = ['url', 'user', 'product', 'rating', 'comment', 'created_at']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    userrating_set = UserRatingSerializer(many=True)
    class Meta:
        model = Product
        fields = ['url', 'owner', 'shop', 'name', 'description', 'price',
                  'rating_count', 'rating_average', 'coupon', 'userrating_set']
        read_only_fields = ['rating_average', 'rating_count', 'users_ratings']
        
class ShopProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    product_set = ShopProductSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = ['url','owner', 'name', 'country', 'email',
                  'phone_number', 'about', 'created_at', 'product_set']
        depth = 0

