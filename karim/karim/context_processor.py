from django.conf import settings


def shop_info(request):

    count = 0
    try:
        if request.session['bucket']:
            count = 0
    except KeyError:
        request.session['bucket'] = []
    

    return {
        'shop_count': count
    }
