import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    n_samples, n_features = (np.array(X)).shape
    mean = np.mean(X, axis = 0)
    X_c = np.array(X) - np.array(mean)
    sigma = (X_c.T@X_c)/(n_samples - 1)
    return sigma
    pass