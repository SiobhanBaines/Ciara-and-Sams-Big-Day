# from decimal import Decimal
# from django.conf import settings


def gift_amount(request):

    gift_amount = request.session.get('gift_amount', {})
    # gift_amount = float(amount)
    # group_id = request.session.get('group_id', {})
    # group = request.session.get('group_id', {})
    # print('contexts group', group)
    context = {
        'gift_amount': gift_amount,
        # 'group_id': group_id,
    }

    # print(gift_amount(type), gift_amount, amount(type), amount)

    return context