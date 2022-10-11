import string_utils as su

def test_get_initials_John_Samuel_Wobbly():
    full_name = 'John Samuel Wobbly'
    expected = 'J.S.W.'
    actual = su.get_initials(full_name)
    assert expected == actual

def test_get_initials_Dylan_McDermott():
    full_name = 'Dylan McDermott'
    expected = 'D.M.'
    actual = su.get_initials(full_name)
    assert expected == actual

def test_get_initials_Norah_Young():
    full_name = 'Norah Young'
    expected = 'N.Y.'
    actual = su.get_initials(full_name)
    assert expected == actual

def test_get_initials_Norah_Young_extra_space():
    full_name = 'Norah  Young'
    expected = 'N.Y.'
    actual = su.get_initials(full_name)
    assert expected == actual