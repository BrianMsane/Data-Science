from math import exp


def linear(x: float | int):
    return x


def sigmoid(x: float | int) -> float:
    return 1 / (1 + exp(-x))


def relu(input: float | int) -> float:
    return max(0, input)


def hyperbolic_tangent(x: float | int) -> float:
    # confirm this formula
    return (1 + exp(-2(input))) / (1 - exp(-2(input)))


def softmax(logits: list[float | int]):
    exponetials = [exp(pred - max(logits)) for pred in logits]
    return [j / sum(exponetials) for j in exponetials]
