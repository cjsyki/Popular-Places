import populartimes;

temp = open( "places.txt", "r" );
text = temp.read( ).split( "id: ");
temp.close( );

placeID = "";
currentHour = "";
currentDay = "";
closedString = "No places are open"
#(40.733400, -73.995484), (40.735847, -73.993542)

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

findBestPlace( 23, "Friday", 40.733441, -73.995186 );