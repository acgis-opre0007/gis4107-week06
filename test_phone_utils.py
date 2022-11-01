import phone_utils as pu

def test_is_valid_phone_number(phone_number):
    return pu.is_valid_phone_number(phone_number)

print(f'\nExpected: True \nActual: {test_is_valid_phone_number("123-456-7890")}')
print(f'\nExpected: True \nActual: {test_is_valid_phone_number("999-999-9999")}')