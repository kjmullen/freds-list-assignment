from api.views import DetailUpdateDeleteListing, ListCreateListing, DetailUser, \
    DetailCategory, DetailCity, ListUser, ListCity, ListCategory, \
    ListSubCategory, DetailSubCategory
from django.conf.urls import url

urlpatterns = [
    url(r"^listings/$", ListCreateListing.as_view(), name="list_create_listing"),
    url(r"^listings/(?P<pk>\d+)/$", DetailUpdateDeleteListing.as_view(),
        name="detail_update_delete_listing"),
    url(r'^users/$', ListUser.as_view(), name="list_user"),
    url(r"^users/(?P<pk>\d+)/$", DetailUser.as_view(), name="detail_user"),
    url(r'^categories/$', ListCategory.as_view(), name="list_category"),
    url(r"^categorories/(?P<pk>\d+)/$", DetailCategory.as_view(),
        name="detail_category"),
    url(r'^subcategories/$', ListSubCategory.as_view(), name="list_subcategory"),
    url(r"^subcategories/(?P<pk>\d+)/$", DetailSubCategory.as_view(),
        name="detail_subcategory"),
    url(r'^cities/$', ListCity.as_view(), name="list_city"),
    url(r'^cities/(?P<pk>\d+)/$', DetailCity.as_view(), name="detail_city"),
]