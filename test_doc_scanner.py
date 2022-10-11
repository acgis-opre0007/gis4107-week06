import doc_scanner

def test_has_x_code(in_text):
    return(doc_scanner.has_x_code(in_text))

def test_get_x_code_position(in_text):
    return(doc_scanner.get_x_code_position(in_text))

print(f'\nExpected: False\nActual: {test_has_x_code("Hello")}')
print(f'\nExpected: True\nActual: {test_has_x_code("Tx6op3")}')

print(f'\nExpected: -1\nActual: {test_get_x_code_position("Hello")}')
print(f'\nExpected: 1\nActual: {test_get_x_code_position("Tx6op3")}')
print(f'\nExpected: 8\nActual: {test_get_x_code_position("Extend Tx6op3")}')