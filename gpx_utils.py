def get_coords_from_gpx(gpx):
    if gpx.startswith('<trpkt lat'):
        coord = gpx.split('"')
        lat = coord.rpartition('"')
        lon = coord.lpartition('"')
        return f'({lat,lon})'
    else:
        return None, None

get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">')