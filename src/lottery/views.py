from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status



class ActivityView(GenericAPIView):
    """"
        used to get the activity info and prize info
    """

    pass


class LotteryView(GenericAPIView):
    """
        used to deal with the post request to create lottery info
    
    
    """
    pass

class LotteryPublicView(GenericAPIView):
    """
        used to compute the prize lottery number 
    """