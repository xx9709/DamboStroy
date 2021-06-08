from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('team', views.team, name="team"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)