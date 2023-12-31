from django.urls import path

from ads.views import category

urlpatterns = [
    path("data/", category.CategoryDataView.as_view()),
    path("", category.CategoryListView.as_view()),
    path("<int:pk>/", category.CategoryDetailView.as_view()),
    path("create/", category.CategoryCreateView.as_view()),
    path("<int:pk>/update/", category.CategoryUpdateView.as_view()),
    path("<int:pk>/delete/", category.CategoryDeleteView.as_view())
]
