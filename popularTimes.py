import populartimes;
import requests;
import datetime;

temp = open( "places.txt", "r" );
text = temp.read( ).split( "id: ");
temp.close( );

temp = open( "zipToCoord.txt", "r" );
lines = temp.readlines( );
temp.close( );

placeID = "";
currentHour = "";
currentDay = "";
closedString = "No places are open"
#(40.733400, -73.995484), (40.735847, -73.993542)


def converter( zip ):
    for address in lines:
        if address[ 0:5 ] == zip:
            return address[ 6:-2 ].split( ", " );

# creates a dictionary of places within a box, makes a new dictionary with all the places along w their popularity at hour hour, and returns best place
def findBestPlace( hour, day, lat, long ):
    #create big dictionary using api
    bigList = populartimes.get("AIzaSyBo8toIXI4IvGZdvvpRtW9Pgf23ub1sVIg", ["bar"], ( lat - 00.002500, long - 00.001000 ), ( lat + 00.002500, long + 00.001000 ) )
    newDict = { };      #new dictionary
    for dicti in bigList:       # for each element in the big dictinary
        name = str( dicti[ "name" ] )       #store id of the location temporarily
        for days in dicti[ "populartimes" ]:    #for each day in the populartimes key
            if days[ "name" ] != day:   # if you arent at the current day, continue to next day
                continue;
            newDict[ name ] = days[ "data" ][ hour ];  #store places id as key and places populartiy at hour hour as value
            break;
    print( newDict ); #test print
    print( lowestValue( newDict ) );
    return( lowestValue( newDict ) );

#returns key with lowest value in a dictionary
def lowestValue( dictionary ):
    minKey = ""
    minVal = 101;
    for key, value in dictionary.items( ):
        if value < minVal and value != 0:           #does not equal zero bc ITS CLOSED!!!
            minVal = value;
            minKey = key;
    if minKey == "":
        return closedString;
    return minKey


timeZoneKey = "AIzaSyDlGb9D4KfSf-Qr1M1_xCw9TQxIVmudbuM";

# coords = converter( "10003" )
# lat = float( coords[ 0 ] );
# long = float( coords[ 1 ] );
# i = datetime.datetime.now( );
# days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ];
# day = days[ i.weekday( ) ]
# hour = i.hour;
# URL = "https://maps.googleapis.com/maps/api/timezone/json?location=" + str( lat) + "," + str( long ) + "&timestamp=${moment().unix()}&key=" + timeZoneKey;
# URL = "https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=" + timeZoneKey;
# r = requests.get( URL )
# print( r.json( ) );
# findBestPlace( hour, day, lat, long );