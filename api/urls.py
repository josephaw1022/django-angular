
from django.urls import path
from api.views import AccountDetail, AccountList, api_root

urlpatterns = [
    path('', api_root, name="api-root"),
    path('Accounts', AccountList.as_view(), name="accounts-list"),
    path('Accounts/<int:pk>/', AccountDetail.as_view(), name="accounts-detail")
]
