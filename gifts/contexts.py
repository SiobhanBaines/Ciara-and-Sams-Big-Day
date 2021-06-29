from decimal import Decimal
from django.conf import settings

def gift_amount(request):

    gift_amount = 0

    context = {
        'gift_amount': gift_amount,
    }

    return context
