

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import (
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
    ProductByIdView,
    ListProductView
)

urlpatterns = [
    path("create-product", 
         CreateProductView.as_view(), 
         name="create-product"
        ),
    path("update-product/<int:id>/", 
         UpdateProductView.as_view(), 
         name="update-product"
        ),
    path("delete-product/<int:pk>/", 
         DeleteProductView.as_view(), 
         name="delete-product"
        ),
    path("product-by-id/<int:pk>/", 
         ProductByIdView.as_view(), 
         name="product-by-id"
        ),
    path("list-product", 
         ListProductView.as_view(), 
         name="list-product"
        ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    