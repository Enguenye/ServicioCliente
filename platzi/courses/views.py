
from django.http import HttpResponse
from urllib.request import urlopen
import hmac
import hashlib
import base64


def get_data(request):
    url = 'http://youtube.com'

    page = urlopen(url)
    llaveS = page.read()

    url2 = 'http://youtube.com'

    page2 = urlopen(url2)
    hash = page2.read()

    url3 = 'http://youtube.com'

    page3 = urlopen(url3)
    documento = page3.read()
    h = hmac.new(llaveS, documento, hashlib.sha256)
    html = documento
    print(h.hexdigest())
    print(hash)
    return HttpResponse(html)
