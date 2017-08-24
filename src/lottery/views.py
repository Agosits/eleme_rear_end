from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from lottery.models import ActivityInfo, PrizeInfo, UserLottery, UserCount
from lottery.utils import lottery_algorithm


class ActivityView(GenericAPIView):
    """"
        used to get the activity info and prize info
    """

    def get(self, request):

        current_day = datetime.date.today()
        activitys = ActivityInfo.objects.filter(start_time_lte=current_day, end_time_gte=current_day)
        prizes_list = []
        for item in activitys:
            prizes = PrizeInfo.objects.get(activity=item)
            activity_info = {}
            activity_info["activity_id"] = item.id
            activity_info["start_time"] = item.start_time
            activity_info["end_time"] = item.end_time
            activity_info["public_time"] = item.public_time
            activity_info["prize_info"] = []
            for prize in prizes:
                prize_info = {"prize_id": prize.id, "prize_name": prize.prize_name, "prize_count": prize.prize_count}
                activity_info["prize_info"].append(prize_info)
            prizes_list.append(activity_info)
        return Response({"activity_info": prizes_list})


class LotteryView(GenericAPIView):
    """
        used to deal with the post request to create lottery info
    
    
    """

    def post(self, request, prize_id):
        percent = 0
        lottery_row = UserLottery.objects.create(user=request.user, prize_info=prize_id)
        prize_row = PrizeInfo.objects.get(pk=prize_id)
        prize_row.prize_lottery_total += 1
        lottery_row.user_lottery_number = prize_row.prize_lottery_total
        user_lottery_number = lottery_row.user_lottery_number
        prize_row.save()
        lottery_row.save()
        try:
            UserCount.objects.create(user=request.user, number=1, percent=0)
        except Exception as e:
            exist_user_count = UserCount.objects.get(user=request.user)
            exist_user_count.number += 1
            percent = exist_user_count.percent = exist_user_count.number \
                                                 // (len(UserCount.objects.all()) + 1)
            exist_user_count.save()
        return Response({"user_lottery_number": user_lottery_number,
                         "user_lottery_percent": percent})


class LotteryPublicView(GenericAPIView):
    """
        used to compute the prize lottery number 
        and write the user lottery table to show who have won
    """

    def get(self, request, activity_id):
        activity = ActivityInfo.objects.get(pk=activity_id)
        for prize in PrizeInfo.objects.get(activity=activity):
            prize_lottery_number = lottery_algorithm(activity.sh_args, activity.sz_args, prize.prize_lottery_total)
            prize.prize_lottery_number = prize_lottery_number
            prize.save()
            for user_lottery in UserLottery.objects.filter(prize_info=prize, user_lottery_number=prize_lottery_number):
                user_lottery.is_winning = True
                user_lottery.save()
