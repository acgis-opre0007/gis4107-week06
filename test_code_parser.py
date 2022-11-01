import code_parser

def test_get_db_link(building_code):
    """
    Tests function get_db_link.
    """

    return(code_parser.get_db_link(building_code))

print(f"\nExpected: BO-642\nActual: {test_get_db_link('20-WBO-109642-809')}")