'''
This is a sample program in python that gives turn by turn directions in a readable format.
In order to code this program please follow the steps below:
1. Go to https://developers.google.com/api-client-library/python/
    This explains what the API is and how it can be used.
2. Click "Get Started" and It will bring you to this link: https://developers.google.com/api-client-library/python/start/get_started
    Here, follow the steps to sign up or login to your Google account and obtain an API key and install the googlemaps library.
    Please follow all the steps as you need to have the Googlemaps library installed on your computer in order to run this program.
3.
'''
import googlemaps
import json, urllib
from urllib import urlencode
import re
import os.path
#authorizing client using key
gmaps = googlemaps.Client(key='AIzaSyB_VMjaJzWr9U6RatHtmJBoSrEbOWgC7vg')
start = raw_input('Enter the address you are departing from: ')
finish = raw_input('Enter the address of the desination: ')
url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
    ('origin', start),
    ('destination', finish)
))
ur = urllib.urlopen(url)
result = json.load(ur)
for i in range (0,len (result['routes'][0]['legs'][0]['steps'])):
    uglyDirections = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    niceDirections = re.sub('<[^>]*>','',uglyDirections)
    print niceDirections