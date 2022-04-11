from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('collections/', views.categories, name="categories"),
    path(
        'collections/<slug:category_slug>/<slug:product_slug>/',
        views.product_detail, name="product_detail"
    ),
    path(
        'collections/<slug:slug>/',
        views.category_product,
        name="category_page"
    ),
]
