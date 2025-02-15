from activation_functions import sigmoid, relu, hyperbolic_tangent
from typing import Literal


def neuron(
    inputs: list[float],
    weights: list[float],
    bias: float,
    function: Literal["relu", "sigmoid", "tanh"] = "relu",
):

    output = (
        sum(input * weight for input, weight in zip(inputs, weights, strict=True))
        + bias
    )
    if function == "relu":
        output = relu(output)
    elif function == "tanh":
        output = hyperbolic_tangent(output)
    else:
        output = sigmoid(output)
    return output


def layer_neuron(inputs: list, weights: list, biases: list[float]):
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
