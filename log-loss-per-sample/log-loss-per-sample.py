import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    result = []
    for i in range(len(y_true)):
        p_hat = min(1-eps, max(eps,y_pred[i]))
        L = -(y_true[i]*math.log(p_hat) + (1-y_true[i])*math.log(1-p_hat))
        result.append(L)
    return result
    pass