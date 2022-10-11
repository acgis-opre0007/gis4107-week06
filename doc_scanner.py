def has_x_code(in_text):
    """Given a string, checks whether a certain series of characters is in the string.
    in_text -- initial string"""

    return('Tx6op3' in in_text)

def get_x_code_position(in_text):
    if ('Tx6op3' in in_text) == True:
        return(in_text.find('Tx6op3')+1)
    else:
        return(-1)