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

@ask.intent( "WhereYouWannaGo", convert = { "place": str, "time": str, "zipcode": str } )
def start( place, time, zipcode ):
    print( str( place ) );
    location = get_alexa_location()
    names = []
    if zipcode is None:
        zipcode = str( location[ "postalCode" ] );
    if time is None:
        names = main( zipcode, place, 25 );
    else:
        names = main( zipcode, place, int( time[ 0:2 ] ) );
    print( names )
    if len( names ) == 0:
        return statement( popularTimes.closedString );
    if len( names ) == 1:
        return question( render_template( "response", name = names[ 0 ][ 0 ], rating = names[ 0 ][ 1 ] ) );
    if len( names ) == 2:
        return question( render_template( "response2", name = names[ 0 ][ 0 ], rating = names[ 0 ][ 1 ], name2 = names[ 1 ][ 0 ], rating2 = names[ 1 ][ 1 ] ) );
    return question( render_template( "response3", name = names[ 0 ][ 0 ], rating = names[ 0 ][ 1 ], name2 = names[ 1 ][ 0 ], rating2 = names[ 1 ][ 1 ], name3 = names[ 2 ][ 0 ], rating3 = names[ 2 ][ 1 ] ) );

@ask.intent( "Rating" )
def rating( name ):
    rating = popularTimes.findRating( name );
    return statement( render_template( "ratingResponse", name = nameOfPlace, rating = rating ) );

@ask.intent( "Location" )
def location( ):
    return;

#10034
def main( zipcode, place, hour ): 
    coords = popularTimes.converter( zipcode )
    lat = float( coords[ 0 ] );
    long = float( coords[ 1 ] );
    i = datetime.datetime.now( );
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ];
    day = days[ i.weekday( ) ]
    if hour == 25:
        hour = i.hour;
    names = popularTimes.findBestPlace( hour, day, lat, long, place );
    print( "main ", names )
    return names;

if __name__ == '__main__':
    app.run(debug=True)
