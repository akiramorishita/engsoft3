def sum(a, b):
    return float(a) + float(b)

def sub(a, b):
    return float(a) - float(b)

def mult(a, b):
    return float(a) * float(b)

def div(a, b):
    return float(a) / float(b)

def exp(a, b):
    return float(a) ** float(b)

def test_sum():
    assert sum(5,3) == 8

def test_sub():
    assert sub(5,3) == 2

def test_mult():
    assert mult(5,3) == 15

def test_div():
    assert div(9,3) == 3