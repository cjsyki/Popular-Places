import logging
import requests
import popularTimes;
import datetime;
from flask import Flask, render_template
from flask_ask import Ask, statement, context

app = Flask(__name__)
ask = Ask(app, '/')
log = logging.getLogger('flask_ask').setLevel(logging.DEBUG)

zipcode = "";

def get_alexa_location():
    URL =  "https://api.amazonalexa.com/v1/devices/{}/settings" \
           "/address".format(context.System.device.deviceId)
    TOKEN =  context.System.user.permissions.consentToken
    HEADER = {'Accept': 'application/json',
             'Authorization': 'Bearer {}'.format(TOKEN)}
    r = requests.get(URL, headers=HEADER)
    if r.status_code == 200:
        return(r.json())

@ask.launch
def launch():
    return start()

@ask.intent("WhereYouWannaGo")
def start():
    msg = render_template( "where" );
    location = get_alexa_location()
    name = main( str( location[ "postalCode" ] ) );
    if name == popularTimes.closedString:
        return statement( popularTimes.closedString );
    print( "you should go to: " + name );
    return statement( "you should go to: " + name );

def main( zipcode ): 
    coords = popularTimes.converter( zipcode )
    lat = float( coords[ 0 ] );
    long = float( coords[ 1 ] );
    i = datetime.datetime.now( );
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ];
    day = days[ i.weekday( ) ]
    hour = i.hour;
    name = popularTimes.findBestPlace( hour, day, lat, long );
    return name;

if __name__ == '__main__':
    app.run(debug=True)
