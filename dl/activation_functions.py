import numpy as np


def linear(x: float | int):
    return x


def sigmoid(x: float | int) -> float:
    return 1 / (1 + np.exp(-x))


def relu(input: float | int) -> float:
    return max(0, input)


def hyperbolic_tangent(x: float | int) -> float:
    return (np.exp(x) - np.power(x, -x))/(np.exp(x) + np.exp(-x))


def softmax(logits: list[float | int]):
    exponetials = [np.exp(pred - max(logits)) for pred in logits]
    return [j / sum(exponetials) for j in exponetials]
