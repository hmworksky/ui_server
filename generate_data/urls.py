from django.conf.urls import url
from generate_data.views import SendView


urlpatterns = [
    url("data/", SendView.as_view()),
]
