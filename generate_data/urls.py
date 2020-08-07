from django.conf.urls import url
from generate_data.views import SendView, SendDetailView


urlpatterns = [
    url("data/", SendView.as_view()),
    url("detail/", SendDetailView.as_view()),
]
