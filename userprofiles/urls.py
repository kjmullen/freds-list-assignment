from django.conf.urls import url
from userprofiles.views import UpdateProfile, UserListings, DeleteListing, \
    UpdateListing

urlpatterns = [

    url(r'^account/delete-listing/(?P<pk>\d+)/$', DeleteListing.as_view(),
        name="delete_listing"),
    url(r'^account/update-listing/(?P<pk>\d+)/$', UpdateListing.as_view(),
        name="update_listing"),
    url(r'^(?P<pk>\d+)/update/$', UpdateProfile.as_view(),
        name="update_profile"),
    url(r'^account/', UserListings.as_view(), name="user_listings"),

]