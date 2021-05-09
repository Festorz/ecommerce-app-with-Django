from django.urls import path

from Commerce import views

app_name = 'commerce'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('clothes/', views.GetClothes.as_view(), name='clothes'),
    path('furniture/', views.GetFurniture.as_view(), name='furniture'),
    path('foodstuff/', views.GetFoodstuff.as_view(), name='foodstuff'),
    path('electronics/', views.GetElectronic.as_view(), name='electronic'),
    path('rentals/', views.GetRental.as_view(), name='rental'),
    path('signup/', views.UserSignUp.as_view(), name='account_signup'),
    path('my_account/', views.TransactionSummaryView.as_view(), name='my-account'),
    path('upload/', views.UploadItem.as_view(), name='upload'),
    path('products/<slug>/', views.ItemDetailView.as_view(), name='products'),
    path('edit-product/<slug>/', views.edit_item, name='edit_product'),
    path('remove-product/<slug>/', views.remove_item, name='remove_product'),
    path('view-seller/<user>/', views.view_seller, name='view_seller'),

]
