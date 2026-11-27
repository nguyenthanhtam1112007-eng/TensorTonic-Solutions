import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    result = []
    for i in x:
        if i > 0:
            result.append(i)
        else:
            result.append(alpha*(math.e**i - 1))
    return result
    pass
    