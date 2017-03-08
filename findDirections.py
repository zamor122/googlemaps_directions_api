######################################################################
#Program that prints directions from a starting point to a destination until user quits
# Author: @Shayne_Zamora
######################################################################
import googlemaps
import json, urllib
from urllib import urlencode
import re
import os.path
#authorizing client using key
gmaps = googlemaps.Client(key='AIzaSyB_VMjaJzWr9U6RatHtmJBoSrEbOWgC7vg')
def sendRequest():
    #Get starting point
    start = raw_input('Enter the address you are departing from: ')
    #Get ending destination point
    finish = raw_input('Enter the address of the desination: ')
    #request from the google url using start and destination points
    request = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
        ('origin', start),
        ('destination', finish)
    ))
    #store request results
    requestResults = urllib.urlopen(request)
    #results in json form
    result = json.load(requestResults)
    #sort json form and print out directions nicely so they are readable
    for i in range (0,len (result['routes'][0]['legs'][0]['steps'])):
        uglyDirections = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
        niceDirections = re.sub('<[^>]*>','',uglyDirections)
        print '\n'+ niceDirections
#main function
def main():
    running = True
    directionNumber = 1
    while running:
        #get directions
        sendRequest()
        #ask user if they would like to get more directions
        answer = raw_input('Would you like to another set of directions? Y or N')
        if answer.upper() == 'N':
            #process exiting
            print 'Process exited Successfully'
            running = False
            break
        else:
            #continue with new directions
            directionNumber+=1
            print 'Please follow the directions below. This is your' , directionNumber , 'time getting directions.'
#run main
main()
