from django.conf.urls import url

from lottery import views as lottery_views

urlpatterns = [
    url(_(r'^submit/$'), lottery_views.LotteryView.as_view(), name='lottery'),
]
