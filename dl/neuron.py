import numpy as np
from utils import activation_function


def neuron(
    inputs: np.array,
    weights: np.array,
    bias: float,
):
    """
    In deep learning, a neuron takes input and calculates the product of them with the weights
    After that, at adds a bias into the sum of
    To introduce non-linerarity, the neuron applies an activation function and the releases in outputs
    """
    summation = (
        sum(input * weight for input, weight in zip(inputs, weights, strict=True))
        + bias
    )
    return activation_function(summation, "sigmoid")


def layer_neuron(
    inputs: list,
    weights: list,
    biases: list[float],
):
    """Run all the neurons that are in the layer and get its output"""
    layer_output = []
    for weights, bias in zip(weights, biases, strict=True):
        output = neuron(inputs=inputs, weights=weights, bias=bias)
        layer_output.append(output)
    return layer_output


def main():
    inputs = [0.1, 0.5]
    print(
        "The ouput of the neuron is: ",
        neuron(inputs=inputs, weights=[0.2, 0.4], bias=0.25),
    )

    biases = [[0.25, 0.25], [0.35, 0.35]]
    weights_list = [[0.1, 0.3], [0.2, 0.4]]
    print("The output of the layer is", layer_neuron(inputs, weights_list, biases[0]))


if __name__ == "__main__":
    main()
