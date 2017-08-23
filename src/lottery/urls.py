from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from lottery import views as lottery_views

urlpatterns = [
    url(_(r'^lottery/$'), lottery_views.ActivityView.as_view(), name='lottery'),
    url(_(r'^lottery/submit/(?P<prize_id>.+)/$'), lottery_views.LotteryView.as_view(), name='lottery'),
]
