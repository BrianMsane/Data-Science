from activation_functions import sigmoid
from errors import total_error


def neuron(inputs: list[float], weights: list[float], bias: float):
    """Each neuron in a nerual network does the following:
    1. Multiply the inputs it gets with its weight
    2. Adds a bias
    3. Applies an activation function to introduce non-linearity
    """
    output = 0
    for input, weight in zip(inputs, weights, strict=True):
        output += input * weight
    return sigmoid(output + bias)


def layer_neuron(inputs: list, weights: list, biases: list[float]):
    """Run all the neurons that are in the layer"""
    layer_output = []
    for weights, bias in zip(weights, biases, strict=True):
        output = neuron(inputs=inputs, weights=weights, bias=bias)
        layer_output.append(output)
    return layer_output


def network(initial_inputs: list[float], weights: list[float], biases: list[float]):
    """assuming a fully connected network, run all the layers and get the final output"""
    pass


def main():
    inputs = [0.1, 0.5]
    weights = [0.2, 0.4]
    bias = 0.25
    print("The ouput of the neuron is: ", neuron(inputs, weights, bias))

    biases = [0.25, 0.25]
    weights_list = [[0.1, 0.3], [0.2, 0.4]]
    print("The output of the layer is", layer_neuron(inputs, weights_list, biases))

    # targets = [0.05, 0.95]
    # network_output = None
    # print("The total error is: ", total_error(target=targets, output=network_output))


if __name__ == "__main__":
    main()
