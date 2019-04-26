
from django.http import HttpResponse
from urllib.request import urlopen
import hmac
import hashlib
import base64


def get_data(request):
    url = 'http://3.91.236.55:8000/courses/llave'

    page = urlopen(url)
    llave1 = str('AVWLyoRfTAfBACuJ0YZ')
    b = bytearray()
    b.extend(map(ord, llave1))

    url2 = 'http://3.91.236.55:8000/courses/solicitarReporte'

    page2 = urlopen(url2)
    documento = str(page2.read()).split("'")[1]

    url3 = 'http://3.91.236.55:8000/courses/solicitarReporteHash'
    page3 = urlopen(url3)
    hash1 = page3.read()
    h = hmac.new(b, str(documento).encode(), hashlib.sha256)
    html = "Reporte:" + documento + "//Integridad--->"
    if str(hash1).split("'")[1] == h.hexdigest():
        html += 'No se ha modificado el mensaje'
    else:
        html += 'Se modificó el mensaje'
    html += " El hash recibido fue: " + h.hexdigest()
    return HttpResponse(html)
