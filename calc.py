def add(x, y):
    """Add function"""
    return x + y
def subtraction(x, y):
    """Subtract function"""
    return x - y
def multiply(x, y):
    """Multiply function"""
    return x * y
def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Can`t be divided by zero")
    return x / y
