def dms2dd(initial_record_dms):
    """
    Given a record of latitude and longitude in degrees-minutes-seconds format, DDD MM SS W|E DD MM SS N|S,
    returns a comma-separated record of latitude and longitude as a string in decimal-degrees.
    initial_record_dms -- input record in DMS
    """

    record_dd = ''
    #initial_record_dms = str(initial_record_dms.splitlines()[0])
    long = 0
    lat = 0

    if len(initial_record_dms) == 22:   #checks for valid length, as in DDD MM SS W|E DD MM SS N|S
        working_elements = initial_record_dms.split(' ') #DMS string is split into list

        for i in range(0,len(working_elements)): #iterates through full list
            if i == 3: #east-west direction item
                if working_elements[i] != 'E' or 'e' or 'W' or 's': #checks if direction is not valid
                    print("ERR 1")
                    return('None, None')
            elif i == 7: #north-south direction item
                if working_elements[i] != 'N' or 'n' or 'S' or 's':
                    print("ERR 2")
                    return('None, None')
            else: #all other non-directional items, which should be numbers
                if working_elements == False:
                    print("ERR 3")
                    return('None, None')
        
        for i in range(0,3): #iterates through longitude deg/min/sec and converts to decimal
            long = long + int(working_elements[i])/(60**i)
        
        for i in range(0,3): #iterates through latitude deg/min/sec and converts to decimal
            lat = lat + int(working_elements[4+i])/(60**i)
        
        if long > 180 or long < 0 or lat > 90 or lat < 0: #checks resultant values against domain
            print("ERR 4")
            return('None, None') #return value as failure if outside domain
        
        if working_elements[4] == 'S' or 's': #interpret north-south direction as sign
            lat = lat*(-1) #south as negative
        
        if working_elements[3] == 'W' or 'w': #interpret east-west direction as sign
            long = long*(-1) #west as negative
        
        record_dd = str(long) + ", " + str(lat)
        
        return(record_dd)
    else:
        print("ERR 5")
        return('None, None') #return value as failure if not of valid length