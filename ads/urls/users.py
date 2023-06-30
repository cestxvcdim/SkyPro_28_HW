from django.urls import path

from ads.views import user

urlpatterns = [
    path("data/", user.UserDataView.as_view()),
    path("", user.UserListView.as_view()),
    path("<int:pk>/", user.UserDetailView.as_view()),
    path("create/", user.UserCreateView.as_view()),
    path("<int:pk>/update/", user.UserUpdateView.as_view()),
    path("<int:pk>/delete/", user.UserDeleteView.as_view())
]
