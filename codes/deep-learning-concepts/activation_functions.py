from math import exp


def sigmoid(x: float | int) -> float:
    return 1 / (1 + exp(-x))


def relu(input: float | int) -> float:
    if input > 0:
        return input
    return 0.0


def hyperbolic_tangent(x: float | int) -> float:
    return (exp(input) - exp(-input)) / (exp(input) + exp(-input))
