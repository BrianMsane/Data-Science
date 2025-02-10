def total_error(y_true: list[float], y_pred: list[float]):
    total = 0
    for output, prediction in zip(y_true, y_pred):
        total += 0.5 * (output - prediction) ** 2
    return total


def mse(y_true, y_pred):
    x_mean = sum(y_pred) / len(y_pred)
    y_mean = sum(y_true) / len(y_true)
    # continue the code


# TO DO: implement
# 1. root mean square error
