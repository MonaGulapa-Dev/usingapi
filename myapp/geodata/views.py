from django.shortcuts import render
from django.conf import settings
import json
import requests
from urllib.request import urlopen
from datetime import datetime


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    url = 'https://api.ipdata.co/' + ip_address + '?api-key=' + settings.IP_STACK_KEY
    response = requests.get(url)
    response2 = urlopen(url)
    json_data = response2.read().decode("utf-8")
    geodata = json.loads(json_data)
    language = geodata['languages']
    language = language[0]
    language = language['name']
    currency = geodata['currency']
    currency = 'Name: ' + currency['name'] + '  ' + 'Code: ' + \
        currency['code'] + '  ' + 'Symbol: ' + currency['symbol']
    time_zone = geodata['time_zone']
    timezone = time_zone['name'] + ' ' + \
        time_zone['abbr'] + ' ' + time_zone['offset']
    today_date = time_zone['current_time']
    today_date1 = today_date[:10]
    date_object = datetime.strptime(today_date1, '%Y-%m-%d').date()
    today_is = datetime.strftime(date_object, "%B %d, %Y")
    return render(request, 'geodata/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'continent': geodata['continent_name'],
        'language': language,
        'currency': currency,
        'timezone': timezone,
        'today_is': today_is,

        # 'location': geodata['location'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': settings.GOOGLE_API
    })
