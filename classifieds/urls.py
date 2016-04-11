from classifieds.views import ListingDetail, CityList, \
    NewListing, SubCategoryListings, CategoryListings, IndexView
from django.conf.urls import url


urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/$', ListingDetail.as_view(),
        name="listing_detail"),
    url(r'^cities/$', CityList.as_view(), name="city_list"),
    url(r'^new/$', NewListing.as_view(), name="new_listing"),
    url(r'^sub/(?P<pk>\d+)/$', SubCategoryListings.as_view(),
        name="subcategory_listings"),
    url(r'^cat/(?P<pk>\d+)/$', CategoryListings.as_view(),
        name="category_listings"),
]