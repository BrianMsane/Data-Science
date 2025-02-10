from activation_functions import sigmoid, relu, hyperbolic_tangent
from errors import total_error


def neuron(
    inputs: list[float], weights: list[float], bias: float, function: str = "relu"
):
    """Each neuron in a nerual network does the following:
    1. Multiply the inputs it gets with its weight
    2. Adds a bias
    3. Applies an activation function to introduce non-linearity
    """
    output = 0
    for input, weight in zip(inputs, weights, strict=True):
        output += input * weight
    if function == "relu":
        res = relu(output + bias)
    elif function == "tanh":
        res = hyperbolic_tangent(output + bias)
    else:
        res = sigmoid(output + bias)

    return res


def layer_neuron(inputs: list, weights: list, biases: list[float]):
    """Run all the neurons that are in the layer and get its output"""
    layer_output = []
    for weights, bias in zip(weights, biases, strict=True):
        output = neuron(inputs=inputs, weights=weights, bias=bias)
        layer_output.append(output)
    return layer_output


# def network(inputs: list[float], weights: list[float], biases: list[float]):
#     """Assuming a fully connected network, run all the layers and get the final output"""
#     outputs = []
#     for layer_weights, layer_bias in zip(weights, biases):
#         layer_output = layer_neuron(inputs, layer_weights, layer_bias)
#         outputs.append(layer_output)
#         inputs = layer_output  # inputs of the next layer are the outputs of the current layer
#     return outputs[-1]


def main():
    inputs = [0.1, 0.5]
    print(
        "The ouput of the neuron is: ",
        neuron(inputs=inputs, weights=[0.2, 0.4], bias=0.25),
    )

    biases = [[0.25, 0.25], [0.35, 0.35]]
    weights_list = [[0.1, 0.3], [0.2, 0.4]]
    print("The output of the layer is", layer_neuron(inputs, weights_list, biases[0]))

    # predictions = network(
    #     inputs=inputs,
    #     weights=[[0.1, 0.3], [0.2, 0.4], [0.5, 0.6], [0.7, 0.8]],
    #     biases=biases,
    # )
    # print("The predicted values are: ", predictions)

    # targets = [0.05, 0.95]
    # network_output = None
    # print("The total error is: ", total_error(target=targets, output=network_output))


if __name__ == "__main__":
    main()
