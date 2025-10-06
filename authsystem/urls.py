from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.user_signup, name="user_signup"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name = "user_logout"),
    path("profile/<int:pk>/", views.view_profile, name= "view_profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)