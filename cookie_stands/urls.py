from django.urls import path
from .views import CookieStandList , CookieStanddetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookiestand_list"),
    path("<int:pk>/", CookieStanddetail.as_view(), name="cookiestand_detail"),
]
