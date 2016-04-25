from classifieds.forms import ListingForm
from classifieds.models import Listing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from rest_framework.authtoken.models import Token
from userprofiles.forms import ProfileForm
from userprofiles.models import Profile


class RegisterUser(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class UpdateProfile(LoginRequiredMixin, UpdateView):

    model = Profile
    form_class = ProfileForm
    template_name = "userprofiles/update_profile.html"

    def get_success_url(self):
        return reverse_lazy('userprofiles:user_listings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['token'] = self.request.user.auth_token
        context['profile'] = self.request.user.profile

        return context

    def reset_token(self):
        if "reset" in self.kwargs['token_reset']:
            self.request.user.profile.reset_token()


class UserListings(LoginRequiredMixin, ListView):

    model = Listing
    template_name = 'userprofiles/user_listings.html'
    paginate_by = 15

    def get_queryset(self):
        query = Listing.objects.select_related('user').all()\
            .filter(user=self.request.user) \
            .order_by('-created_at')
        return query


class UpdateListing(LoginRequiredMixin, UpdateView):

    model = Listing
    form_class = ListingForm
    template_name = 'userprofiles/update_listing.html'

    def get_success_url(self):
        return reverse('listing_detail', args=(self.object.id,))


class DeleteListing(LoginRequiredMixin, DeleteView):

    model = Listing
    template_name = "userprofiles/delete_listing.html"
    success_url = reverse_lazy('userprofiles:user_listings')
