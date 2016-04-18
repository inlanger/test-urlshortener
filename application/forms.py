from django import forms
from django.contrib.auth.models import User
from django.conf import settings

from application.models import Entry
from application.utils import key_generator


class AddUrlForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please, enter valid URL to make it shorter'
        }
    ))

    def save(self):
        random_user = User.objects.order_by('?').first()

        return Entry.objects.create(
            url=self.cleaned_data['url'],
            user=random_user,
            key=key_generator(getattr(settings, 'URL_LEN', 6))
        )
