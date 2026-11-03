
def add(a, b):
    validate_inputs(a, b)
    return a + b


def subtract(a, b):
    validate_inputs(a, b)
    return a - b


def multiply(a, b):
    validate_inputs(a, b)
    return a * b


def validate_inputs(a, b):
    if not isinstance(a, int) or isinstance(a, bool):
        raise ValueError("Inputs must be positive integers")

    if not isinstance(b, int) or isinstance(b, bool):
        raise ValueError("Inputs must be positive integers")

    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
