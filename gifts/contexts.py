from decimal import Decimal
from django.conf import settings


def gift_amount(request):

    gift_amount = request.session.get('gift_amount', {})

    context = {
        'gift_amount': gift_amount,
    }

    return context
