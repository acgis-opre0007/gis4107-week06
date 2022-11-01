import dms_converter

def test_dms2dd(initial_record_dms):
    return(dms_converter.dms2dd(initial_record_dms))
print('\n')
print(f'Initial Record: 075 45 03 W 045 23 05 N\nExpected: -75.751, 45.385\nActual: {test_dms2dd("075 45 03 W 045 23 05 N")}\n')
print(f'Initial Record: 075 45 03 L 045 23 05 N (bad east-west indicator)\nExpected: None, None\nActual: {test_dms2dd("075 45 03 L 045 23 05 N")}\n')
print(f'Initial Record: 075 45 03 W 045 23 05 U (bad north-south indicator)\\n\nExpected: None, none\nActual: {test_dms2dd("075 45 03 W 045 23 05 U")}\n')
print(f'Initial Record: yes 45 03 W deg 23 05 N (bad DMS values)\\n\nExpected: -75.751, 45.385\nActual: {test_dms2dd("yes 45 03 W deg 23 05 N")}\n')
print(f'Initial Record: 200 10 10 E 100 10 10 N (outside range domain)\nExpected: None, None\nActual: {test_dms2dd("200 10 10 E 100 10 10 N")}\n')
print(f'Initial Record: Hi (too short)\nExpected: None, None\nActual: {test_dms2dd("Hi")}\n')