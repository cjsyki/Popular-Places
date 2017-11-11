import populartimes;


temp = open( "places.txt", "r" );
text = temp.read( ).split( "id: ");
temp.close( );

for line in text:
    print( line );
# bigList = populartimes.get("AIzaSyBo8toIXI4IvGZdvvpRtW9Pgf23ub1sVIg", ["bar"], (40.733400, -73.995484), (40.735847, -73.993542))

# def printTimes( ):
#     for dicti in bigList:
#         print( "id: " + str( dicti[ "id" ] ) );
#         data = "";
#         for days in dicti[ "populartimes" ]:
#             data += days[ "name" ] + ": ";
#             for hours in days[ "data" ];
#                 data += str( hours ) + " ";
#             print( data );
#             data = "";
    

# printTimes( );