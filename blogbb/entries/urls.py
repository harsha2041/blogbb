
from django.urls import path

from .views import HomeView,EntryView,CreateEntryView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', HomeView.as_view(), name='blog-name'),
    path('entry/<int:pk>/',EntryView.as_view(), name="entry-detail"),
    path('create_entry/',CreateEntryView.as_view(success_url='/'), name="create_entry"),# need to complete
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon_new.ico')))
]
