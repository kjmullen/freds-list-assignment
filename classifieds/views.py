from classifieds.forms import ListingForm
from classifieds.models import Listing, City, Category, SubCategory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    RedirectView, View


def get_city(request):
    city = request.session.get("city", None)

    if hasattr(request.user, 'profile') and hasattr(request.user.profile,
                                                    "city"):
        return request.user.profile.city
    elif request.session.get("city", None):
        return City.objects.get(pk=city.pk)
    else:
        return None


class IndexView(ListView):

    template_name = "classifieds/index.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        context['community_category'] = Category.objects.get(pk=1)
        context['housing_category'] = Category.objects.get(pk=2)
        context['forsale_category'] = Category.objects.get(pk=3)
        context['services_category'] = Category.objects.get(pk=4)
        context['jobs_category'] = Category.objects.get(pk=5)

        return context


class SubCategoryListings(ListView):

    paginate_by = 15
    template_name = "classifieds/subcategory_listings.html"

    def get_queryset(self):
        subcategory = get_object_or_404(SubCategory, pk=self.kwargs['pk'])
        return Listing.objects.select_related('city').all()\
            .filter(subcategory=subcategory)\
            .filter(city=get_city(self.request))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs['pk'])
        return context


class CategoryListings(ListView):

    paginate_by = 15
    template_name = 'classifieds/category_listings.html'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Listing.objects.select_related('city').all().filter(
            subcategory__in=category.subcategories.all()) \
            .filter(city=get_city(self.request))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context


class CityList(ListView):

    model = City
    template_name = "classifieds/city_list.html"


class ListingDetail(DetailView):

    model = Listing
    template_name = "classifieds/listing_detail.html"


class NewListing(CreateView):

    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy("index")
    template_name = "classifieds/new_listing.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SessionCity(RedirectView):
    pattern_name = "redirect_city"

    def get_redirect_url(self, *args, **kwargs):
        session_city = get_object_or_404(City, pk=self.kwargs["pk"])
        self.request.session["city__pk"] = session_city.pk
        if self.request.user.username:
            self.request.user.profile.city = session_city
            self.request.user.profile.save()
        return reverse("index")


