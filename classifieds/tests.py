from classifieds.models import Category, SubCategory, City, Listing
from classifieds.views import IndexView, SubCategoryListings, CategoryListings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from faker import Faker


class TestSetup(TestCase):

    fake = Faker()

    def new_category(self, number=1):
        self.categories = [Category.objects.create(name=self.fake.word())
                           for _ in range(number)]
        return self.categories

    def new_user(self, number=1):
        self.users = [User.objects.create(username=self.fake.word(),
                                          email='',
                                          password=self.fake.word())
                      for _ in range(number)]
        return self.users

    def new_subcategory(self, category, number=1):
        self.subcategories = [SubCategory.objects.create(category=category,
                                                         name=self.fake.word())
                              for _ in range(number)]
        return self.subcategories

    def new_city(self, number=1):
        self.cities = [City.objects.create(name=self.fake.word())
                       for _ in range(number)]
        return self.cities

    def new_listing(self, user, subcategory, city, number=1):
        self.listings = [Listing.objects.create(title=self.fake.word(),
                                                body=self.fake.word(),
                                                price=10,
                                                user=user,
                                                subcategory=subcategory,
                                                city=city)
                         for _ in range(number)]
        return self.listings


class IndexViewTests(TestSetup):

    """
    Hard coded categories in for more custom
    front end setup. Had to make 5 categories
    here because the index calls each by pk
    1-5
    """
    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username='tester', email='', password='password')
        self.user = self.new_user()[0]
        self.new_category(5)
        self.city = self.new_city()[0]

    def test_details(self):
        request = self.factory.get('/')
        request.user = self.user
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class SubCategoryListingsTest(TestSetup):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = self.new_user()[0]
        self.city = self.new_city()[0]
        self.category = self.new_category()[0]
        self.subcategory = self.new_subcategory(category=self.category)[0]
        self.listings = self.new_listing(self.user, self.subcategory,
                                         self.city, 2)
        self.othersubcategory = self.new_subcategory(category=self.category)[0]
        self.otherlistings = self.new_listing(self.user, self.othersubcategory,
                                         self.city, 5)

    def test_details(self):
        request = self.factory.get('/l/sub/1/', data={self.subcategory:
                                                          self.listings})
        request.user = self.user
        request.subcategory = self.subcategory
        request.session = {'city': self.city}
        response = SubCategoryListings.as_view()(request, pk=1)
        subcategory = response.context_data['subcategory']
        self.assertEqual(subcategory.listings.count(), 2)
        self.assertEqual(response.status_code, 200)


# class CategoryListingsTest(TestSetup):
#
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.city = self.new_city()[0]
#         self.user = self.new_user()[0]
#         self.category = self.new_category()[0]
#         self.subcategory = self.new_subcategory(self.category)
#         self.listings = self.new_listing(self.user,
#                                          self.subcategory, self.city, 2)
#
#     def test_details(self):
#         request = self.factory.get('l/cat/1/')
#         request.user = self.user
#         request.session = {'city': self.city}
#         response = CategoryListings.as_view()(request, pk=1)
#         category = response.context_data['category']
#         subcategories = category.subcategory_set
#         self.assertEqual(subcategories.listing_set.count(), 2)
#
#
#



# def test_details(self):
#     # Create an instance of a GET request.
#     request = self.factory.get('/customer/details')
#
#     # Recall that middleware are not supported. You can simulate a
#     # logged-in user by setting request.user manually.
#     request.user = self.user
#
#     # Or you can simulate an anonymous user by setting request.user to
#     # an AnonymousUser instance.
#     request.user = AnonymousUser()
#
#     # Test my_view() as if it were deployed at /customer/details
#     response = my_view(request)
#     # Use this syntax for class-based views.
#     response = MyView.as_view()(request)
#     self.assertEqual(response.status_code, 200)




# import unittest
# from django.test import RequestFactory
#
# class HelloViewTestCase(unittest.TestCase):
#     def test_get(self):
#         """HelloView.get() sets 'name' in response context."""
#         # Setup name.
#         name = 'peter'
#         # Setup request and view.
#         request = RequestFactory().get('/fake-path')
#         view = HelloView.as_view(template_name='hello.html')
#         # Run.
#         response = view(request, name=name)
#         # Check.
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.template_name[0], 'home.html')
#         self.assertEqual(response.context_data['name'], name)