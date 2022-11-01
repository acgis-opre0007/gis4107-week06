def get_db_link(building_code):
    """
    Given a code of the format NN-LLL-NNNNNN-NNN, where N is a number and L is a letter, returns a
    foreign key for joining tables of the format LL-NNN.
    building_code -- initial code
    db_link -- output key
    """
    db_link = building_code[4:7] + building_code[10:13]

    return db_link

