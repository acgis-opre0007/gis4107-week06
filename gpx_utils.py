def get_coords_from_gpx(gpx):
    if gpx.startswith('<trkpt lat'):
        x = gpx.strip('<trkptlat=on> "')
        lat = (x.rsplit('"'))[0]
        lon = (x.rsplit('"'))[2]
        return lat, lon
    else:
        return None, None