import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    result = []
    for i in np.array(x):
        if i >= 0:
            result.append(i)
        else:
            result.append(alpha*i)
    return np.array(result)
    pass