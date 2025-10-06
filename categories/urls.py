from django.urls import path, include
from .views import (
    CreateCategoryView, 
    UpdateCategoryView, 
    DeleteCategoryView,
    CategoryByIdView,
    ListCategoryView
)


urlpatterns = [
    path("create-category", 
         CreateCategoryView.as_view(), 
         name="create_category"
        ),
    path("update-category", 
         UpdateCategoryView.as_view(), 
         name="Update_category"
        ),
    path("delete-category", 
         DeleteCategoryView.as_view(), 
         name="delete_category"
        ),
    path("category-by-id/<int:id>", 
         CategoryByIdView.as_view(), 
         name="delete_category"
        ),
    path("list-category", 
         ListCategoryView.as_view(), 
         name="list-category"
        ),
    
    
]
