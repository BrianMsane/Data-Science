from typing import Union
from .activation_functions import sigmoid


def neuron(input: float, weight: float, bias: float):
    output = 0
    for input, weight in zip(inputs, weights):
        output += input * weight
    return output + bias


def layer_neuron(inputs: list, weights: list, biases: Union[int, float]):
    layer_output = []
    for n_weight, n_bias in zip(weights, biases):
        output = neuron(inputs=inputs, weights=n_weight, bias=n_bias)
        layer_output.append(output)
    return layer_output


if __name__ == "__main__":
    # inputs = [9, 2, 7]
    # weights = [.1, .9, -.5]
    # output = neuron(inputs=inputs, weights=weights, bias=.7)
    # print("The output of this layer is {}".format(output))

    weights = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87],
    ]

    inputs = [1, 2, 3, 2.5]
    biases = [2, 3, 0.5]
    layer_output = layer_neuron(inputs=inputs, weights=weights, biases=biases)
    print("The output of this layer is {}".format(layer_output))
