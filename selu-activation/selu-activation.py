import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    x = np.asarray(x)

    result = np.where(
        x > 0,
        1.0507 * x,
        1.0507 * 1.6733 * np.expm1(x)
    )

    return np.round(result, 4).tolist()
    pass