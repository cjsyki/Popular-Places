import populartimes;

temp = open( "places.txt", "r" );
text = temp.read( ).split( "id: ");
temp.close( );


if len( text ) == 1:
    temp = open( "places.txt", "w" );
    bigList = populartimes.get("AIzaSyBo8toIXI4IvGZdvvpRtW9Pgf23ub1sVIg", ["bar"], (40.733400, -73.995484), (40.735847, -73.993542))
    for dicti in bigList:
        data = "id: " + str( dicti[ "id" ] ) + "\n" ;
        for days in dicti[ "populartimes" ]:
            data += days[ "name" ] + ": ";
            for hours in days[ "data" ]:
                data += str( hours ) + " ";
            data += "\n"
        print( data + "\n" );
        temp.write( data + "\n" );
    temp.close( );
else:
    for line in text:
        print( line );
    