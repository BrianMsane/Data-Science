def total_error(y_true: list[float], y_pred: list[float]):
    total = 0
    for output, prediction in zip(y_true, y_pred):
        total += 0.5 * (output - prediction) ** 2
    return total
