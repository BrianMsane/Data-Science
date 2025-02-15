def mean_squared_error(preds: list, y_true: list):
    return sum([(actual - pred) ** 2 for pred, actual in zip(preds, y_true)]) / len(
        y_true
    )


def root_mean_squared_error(preds: list, y_true: list):
    pass


def mean_absolute_error():
    pass
