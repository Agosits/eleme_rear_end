from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class UserInfo(models.Model):
    """"
    this is a related userinfo table to show the lottery
        user: the id of user account
        score: the score of this user which will be used when submit lottery
    """
    user = models.OneToOneField(User)
    score = models.PositiveIntegerField(default=0)


class PrizeInfo(models.Model):
    """
    this is the table about prize information, which include blow:
      prize_name: the name of prize
      prize_count: the count of this kind of prize, default to be 1
      prize_lottery_number: the lottery number to user who have the same number
        will own this kind of prize, default to be NULL
      prize_lottery_total: the total number of this prize during activity   

    """
    prize_name = models.CharField(_('Prize Name'), max_length=128, null=True, blank=False)
    prize_count = models.IntegerField(_("Prize Count"), default=1)
    prize_lottery_number = models.PositiveIntegerField(_("Prize Lottery Number"), null=True)
    prize_lottery_total = models.PositiveIntegerField(_("Prize Lottery Total"), null=True)
    activity = models.ForeignKey(ActivityInfo, on_delete=models.CASCADE)


class ActivityInfo(models.Model):
    """
     this is the table about activity information, which include blow:
     start_time: the start time of activity
     end_time: the end time of activity
     public_time: the public time to show the lottery number
     sh_args: The Shanghai Composite Index　of public time
     zs_args: Shenzhen Stock Index　of public time
    """
    start_time = models.DateField()
    end_time = models.DateField()
    public_time = models.DateField(null=True)
    sh_args = models.FloatField(null=True)
    sz_args = models.FloatField(null=True)


class UserLottery(models.Model):
    """
    this is the table about lottery of user order, which include blow:
      user: the id of user who submit lottery
      order: the id of order which is created by user
      prize_info: the id of prize when front end submit the kind of lottery prize
      user_lottery_number: the number of this lottery towards prize_info
      is_winning: show whether the lottery is winning
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserInfo, related_name='user_id')
    prize_info = models.ForeignKey(PrizeInfo, related_name="prize_info_id")
    user_lottery_number = models.IntegerField(default=0)
    is_winning = models.BooleanField(default=False)


class UserCount(models.Model):
    """
    this is the table about lottery statistics of user, which include blow:
      user: the id of user who submit lottery
      number: the number of times submitted by user
      percent: the percentage of number of times of whole user who submit lottery
  
    """
    user = models.OneToOneField(UserInfo, unique=True)
    number = models.IntegerField(default=0)
    percent = models.FloatField(default=0)
