from django.contrib import admin
from django.urls import path
from vege import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("reci/", views.reci, name="reci"),
    path("delete_reci/<id>/", views.delete_reci, name="delete_reci"),
    path("update_reci/<id>/", views.update_reci, name="update_reci"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# url = http://127.0.0.1:8000/reci/media/receipi/IMG_4546_1.jpg