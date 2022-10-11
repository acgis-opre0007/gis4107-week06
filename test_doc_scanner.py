import doc_scanner

def test_has_x_code(in_text):
    return(doc_scanner.has_x_code(in_text))

print(f'\nExpected: False\nActual: {test_has_x_code("Hello")}')
print(f'\nExpected: True\nActual: {test_has_x_code("Tx6op3")}')