from activation_functions import sigmoid, relu, hyperbolic_tangent, linear
from typing import Literal


def activation_function(
    input: int | float,
    function: Literal["relu", "sigmoid", "tanh", "linear"] = "relu",
):
    """
    Pass the result of the summation through and activation function

    Args:
        input(int | float): The summation result
        function(str): The activation function to use
    """
    if function == "linear":
        output = linear(output)
    elif function == "relu":
        output = relu(output)
    elif function == "tanh":
        output = hyperbolic_tangent(output)
    else:
        output = sigmoid(output)
    return output
