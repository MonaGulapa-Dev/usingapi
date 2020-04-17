from django.shortcuts import render
from django.conf import settings
import requests, json



def home(request):
    is_cached = ('geodata' in request.session)
    auth=settings.IPFIND_API
    google_api=settings.GOOGLE_API
    iploc = 'https://api.ipfind.com/me?auth=' + auth
    if not is_cached:
        response = requests.get(iploc)
        request.session['geodata'] = response.json()
        # print(type(geodata))  #dict
        # for key in geodata.keys():
        #     value = geodata[key]
        #     print(key, '=', value)

        # # data = json.load(geodata)
        # context = {'geodata1': geodata}
        # print(type(context))
        # for key in context.keys():
        #     value = context[key]
        #     print(key, '=', value)

    geodata = request.session['geodata']

    return render(
        request,
        'geodata/home.html',
        {
            'ip': geodata['ip_address'],
            'country': geodata['country'],
            'city': geodata['city'],
            'region': geodata['region'],
            'timezone': geodata['timezone'],
            'currency': geodata['currency'],
            'languages': geodata['languages'],
            'latitude': geodata['latitude'],
            'longitude': geodata['longitude'],
            'api_key': google_api,
            'is_cached': is_cached
        },
    )
 
