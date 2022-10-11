def get_initials(full_name):
    """_summary_

    Args:
        full_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    initials = ""
    parts = full_name.split()
    first_chars = []
    for part in parts:
        first_chars.append(part[0])
    initials = '.'.join(first_chars)
    initials += '.'
    return initials