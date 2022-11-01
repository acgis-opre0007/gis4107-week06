def is_valid_phone_number(phone_number):
    valid_number = ''.join(phone_number.split('-')) #removes '-', creates list, joins items in list
    if valid_number.isdigit: 
        if len(valid_number) == 10:
            return True
    else:
        return False