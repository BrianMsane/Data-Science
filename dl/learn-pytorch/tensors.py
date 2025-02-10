"""Working with pytorch tensors"""

import torch
import numpy as np
from pprint import pprint

# TO-DO:
# set the seed for deterministic tensors so you can get predictable scores
# setup cuda; download cuda-package from nvidia


# NOTES:
"""
1. You can also change the data type of a tensor by specifying the dtype when creating it
2. Perform basic arithmetic operations with tensors - done element-wise
3. In slicing operations the first slice is for the rows and the last one is for the columns x[: , :]
4. Numpy only handles CPU Tensors; so you cannot convert a GPU tensor to numpy
"""


def different_ways_to_make_tensors():
    tensor = torch.empty(2)
    random_values = torch.rand(2)
    zeros = torch.zeros(2, dtype=torch.double)
    ones = torch.ones(2, dtype=torch.int)
    from_data = torch.tensor([71, 68, 66], dtype=torch.float16)
    return [tensor, random_values, zeros, ones, from_data]


def basic_operations(first: torch.Tensor, second: torch.Tensor):
    """Element-wise operations
    1. Addition (+)
    2. Subtraction (-)
    3. Division
    4. Slicing operation
    5. etc., [Research more on this!]
    """
    first.add(second)
    torch.mul(first.second)
    torch.divide(first, second)
    first[:, 0]  # all rows and column zero
    second[
        1, 1
    ].item()  # only use when you have one item in the resulting tensor; it gets the actual value


def reshape_tensor():
    x = torch.rand(4, 4)
    y = x.view(-1, 8)
    z = y.view(16)
    return z


def numpy_and_tensr_conversion():
    tensor = torch.ones(3)  # you may need to calculate the gradients of this tensor
    numpy_from_tensor = tensor.numpy()
    tensor_from_numpy = torch.from_numpy(numpy_from_tensor)
    print(type(numpy_from_tensor))
    print(type(tensor_from_numpy))


all_tensors = different_ways_to_make_tensors()

# pprint(all_tensors[0])
# pprint(all_tensors[1])
# pprint(all_tensors[2])
# pprint(all_tensors[3])
# pprint(all_tensors[4])

"""
AUTOGRAD
a. Used to calculate gradients which are vital for model optimization
b. 
"""

x = torch.randn(3, requires_grad=True)  # pytorch will create a computational graph
x.add_(2)
