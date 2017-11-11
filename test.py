import populartimes;

temp = open( "places.txt", "r" );
text = temp.read( ).split( "id: ");
temp.close( );

placeID = "";
currentHour = "";
currentDay = "";

#(40.733400, -73.995484), (40.735847, -73.993542)

# creates a dictionary of places within a box, makes a new dictionary with all the places along w their popularity at hour hour, and returns best place
def findBestPlace( hour, day, south_lat, south_long, north_lat, north_long ):
    #create big dictionary using api
    bigList = populartimes.get("AIzaSyBo8toIXI4IvGZdvvpRtW9Pgf23ub1sVIg", ["bar"], ( 40.733400, -73.995484 ), ( 40.735847, -73.993542 ) )
    newDict = { };      #new dictionary
    for dicti in bigList:       # for each element in the big dictinary
        id = str( dicti[ "id" ] )       #store id of the location temporarily
        for days in dicti[ "populartimes" ]:    #for each day in the populartimes key
            if days[ "name" ] != day:   # if you arent at the current day, continue to next day
                continue;
            newDict[ id ] = days[ "data" ][ hour ];  #store places id as key and places populartiy at hour hour as value
            break;
    print( newDict ); #test print
    print( lowestValue( newDict ) );

#returns key with lowest value in a dictionary
def lowestValue( dictionary ):
    minKey = ""
    minVal = 101;
    for key, value in dictionary.items( ):
        if value < minVal:
            minVal = value;
            minKey = key;
    return key

findBestPlace( 23, "Friday" );