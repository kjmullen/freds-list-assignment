from classifieds.models import Listing, Category, SubCategory, City
from django.contrib.auth.models import User
from moneyed import Money
import decimal
from rest_framework import serializers


class MoneyField(serializers.Field):
    default_error_messages = {
        'non_negative': 'The amount must be positive.',
        'not_a_number': 'The amount must be a number.'
    }

    def __init__(self, *args, **kwargs):
        self.non_negative = kwargs.pop('non_negative', False)
        return super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        return obj.amount

    def to_internal_value(self, data):
        try:
            obj = Money(data)
        except decimal.InvalidOperation:
            self.fail('not_a_number')
        if obj < Money('0') and self.non_negative:
            self.fail('non_negative')
        return Money(data)


class UserSerializer(serializers.ModelSerializer):

    listings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'listings')


class CitySerializer(serializers.ModelSerializer):

    listing_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('name', 'id', 'listing_set')


class CategorySerializer(serializers.ModelSerializer):

    subcategory_set = serializers.PrimaryKeyRelatedField(many=True,
                                                         read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategory_set')


class SubCategorySerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    listing_set = serializers.PrimaryKeyRelatedField(many=True,
                                                      read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'category', 'name', 'listing_set')


class ListingSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    price = MoneyField(read_only=True)


    class Meta:
        model = Listing
        fields = '__all__'
