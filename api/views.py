from api.permissions import IsOwnerOrReadOnly
from api.serializers import ListingSerializer, UserSerializer, \
    CategorySerializer, SubCategorySerializer, CitySerializer
from classifieds.models import Listing, Category, SubCategory, City
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DetailUser(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUser(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailCity(generics.RetrieveAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class ListCity(generics.ListAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class DetailCategory(generics.RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailSubCategory(generics.RetrieveAPIView):

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ListSubCategory(generics.ListAPIView):

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ListCreateListing(generics.ListCreateAPIView):

    queryset = Listing.objects.order_by('-created_at')
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()

        params = self.request.query_params
        if "search" in params:
            qs = qs.filter(Q(title__icontains=params['search']) |
                           Q(body__icontains=params['search']))

        return qs


class DetailUpdateDeleteListing(generics.RetrieveUpdateDestroyAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


