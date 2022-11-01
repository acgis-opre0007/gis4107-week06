import dms_converter

def test_dms2dd(initial_record_dms):
    return(dms_converter.dms2dd(initial_record_dms))

print(f'\nInitial Record: Hello World (invalid input)\nExpected: None, None\nActual: {test_dms2dd("Hello World")}')
print(f'\nInitial Record: 075 45 03 W 45 23 05 N\\n\nExpected: -75.751, 45.385\nActual: {test_dms2dd("075 45 03 W 45 23 05 N")}')
#print(f'\nInitial Record: Hello World (invalid input)\nExpected: None, None\nActual: {test_dms2dd("Hello World")}')
#print(f'\nInitial Record: Hello World (invalid input)\nExpected: None, None\nActual: {test_dms2dd("Hello World")}')