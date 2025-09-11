"""Implement common forumas in statistics"""

import math


def mean(numbers: list[int | float]) -> float:
    return sum([num for num in numbers]) / len(numbers)


def mode(data: list):
    pass


def median(data: list):
    pass


def variance(data: list):
    pass


def standard_deviation(data: list[int | float]) -> float:
    return math.sqrt(sum([(num - mean(data)) ** 2 for num in data]) / len(data))


def z_score(data: list[int | float]) -> list:
    mean_value = mean(data)
    std = standard_deviation(data)
    return [((num - mean_value) / std) for num in data]
