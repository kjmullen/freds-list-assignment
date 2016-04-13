from classifieds.models import Listing
from django import forms
from django.forms import Textarea


class ListingForm(forms.ModelForm):

    class Meta:

        model = Listing
        fields = ('title', 'body', 'price', 'phone_num', 'city', 'subcategory',
                  'image')
        widgets = {
            'description': Textarea(attrs={'rows': 4, 'cols': 45})
        }


class SearchForm(forms.Form):

    search = forms.CharField(label='Search', max_length=150)
