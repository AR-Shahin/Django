
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/",include("user.urls")),
    path("orm/",include("orm.urls")),
    path("ecom/",include("ecommerce.urls")),
    path("auth/",include("authentication.urls")),
    path("",include("orm.urls"))
]
