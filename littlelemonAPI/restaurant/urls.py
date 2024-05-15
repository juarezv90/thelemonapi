from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('booking/', views.BookingViews.as_view()),
    path('booking/<int:pk>/', views.SingleBookingView.as_view()),
    path('menu_add/', views.MenuView.as_view()),
    path('menu_add/<int:pk>', views.SingleMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('', views.index, name='index'),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'), 
]