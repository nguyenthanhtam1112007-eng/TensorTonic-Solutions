import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    return np.mean((np.array(y_pred)-np.array(y_true))**2)
    pass