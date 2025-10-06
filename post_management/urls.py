
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create-post/",views.create_post, name= "create_post" ),
    path("create-tags/", views.create_tags, name="create_tags"),
    path("edit/<str:slug>/", views.edit_post, name = "edit_post"),
    path("view/", views.view_post, name="view_post"),
    path("view/<str:slug>/", views.post_details, name = "post_details"),
    path("view/<str:slug>/like/", views.liked_post, name = "liked_post"),
    path("view/categories/<str:slug>/", views.post_category_filter, name = "category_filter"),
    path("categories/", views.view_category, name = "view_category"),
    path("view/<str:slug>/<int:pk>/", views.edit_comment, name = "edit_comment"),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact, name = "contact"),
    path("delete/<str:slug>/", views.delete_post, name = "delete_post"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)