from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#po slashu będzie obsługiwany przez funkcję post_list w pliku views
