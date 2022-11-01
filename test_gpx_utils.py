import gpx_utils as gu

def test_get_coords_from_gpx(gpx):
    return gu.get_coords_from_gpx(gpx)

print(f'''f'\nExpected: 45.3888995,-75.7472631  \nActual: {test_get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">')}''')
print(f'''f'\nExpected: None, None  \nActual: {test_get_coords_from_gpx('"45.3888995" lon="-75.7472631">')}''')