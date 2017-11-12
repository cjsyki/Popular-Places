import logging
import requests
import popularTimes;
import datetime;
from flask import Flask, render_template
from flask_ask import Ask, statement, context, question

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
    whereStr_msg = render_template( 'where' );
    return question( whereStr_msg )
    # return start()

@ask.intent( "WhereYouWannaGo", convert = { "place": str, "time": str } )
def start( place, time ):
    print( str( place ) );
    location = get_alexa_location()
    zipcode = str( location[ "postalCode" ] );
    if time is None:
        name = main( zipcode, place, 25 );
    else:
        name = main( zipcode, place, int( time[ 0:2 ] ) );
    print( "name of the olace!!!!! " + nameOfPlace )
    if name == popularTimes.closedString:
        return statement( popularTimes.closedString );
    return question( render_template( "response", name = name ) );

@ask.intent( "Rating" )
def rating( name ):
    rating = popularTimes.findRating( name );
    return statement( render_template( "ratingResponse", name = nameOfPlace, rating = rating ) );

@ask.intent( "Location" )
def location( ):
    return;

#10034
def main( zipcode, place, hour ): 
    print( zipcode );
    coords = popularTimes.converter( zipcode )
    lat = float( coords[ 0 ] );
    long = float( coords[ 1 ] );
    i = datetime.datetime.now( );
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ];
    day = days[ i.weekday( ) ]
    if hour == 25:
        hour = i.hour;
    name = popularTimes.findBestPlace( hour, day, lat, long, place );
    nameOfPlace = name;
    return name;

if __name__ == '__main__':
    app.run(debug=True)
