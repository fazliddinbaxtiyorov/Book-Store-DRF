from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

urlpatterns = [
    path('api/', views.BookList.as_view()),
    path('api/all', views.AllBookList.as_view()),
    path('api/new', views.AddBook.as_view()),
    path('api/<int:id>', views.BookDetail.as_view()),
    path('api/<int:id>/delete', views.BookDelete.as_view()),
    path('api/<int:id>/updata', views.BookUpdate.as_view()),
    path('api/<username>/', views.User_Blog_Search.as_view()),
    path('api/sort', views.SortedBookList.as_view()),
    path('signup/', views.SignUp.as_view()),
    path('api/login', views.LoginView.as_view()),
    path('api/subscribe', views.Subscribes.as_view()),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/password_reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('api/password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


