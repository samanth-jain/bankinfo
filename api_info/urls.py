from django.urls import path
from .views import Branch_SearchView, Bank_SearchView, BankListView, HomeView

urlpatterns = [
    path('home/', HomeView , name = 'home'),
    path('branch/get/', Branch_SearchView.as_view(), name='branch-search'),
    path('bank/get/', Bank_SearchView.as_view(), name='bank-search'),
    path('bank/list/', BankListView.as_view(), name='bankdetail'),
]