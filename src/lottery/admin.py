from django.contrib import admin
from lottery.models import PrizeInfo, ActivityInfo

class PrizeInfoAdmin(admin.ModelAdmin):
    fields = ("prize_name", "activity")


class ActivityInfoAdmin(admin.ModelAdmin):
    fields = ("start_time", "end_time", "public_time")


admin.site.register(PrizeInfo, PrizeInfoAdmin)

admin.site.register(ActivityInfo, ActivityInfoAdmin)