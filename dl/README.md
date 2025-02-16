# Neural Networks

Deep learning uses neurons as the basic building block!

## A Single Neuron

Each neuron is capable of doing the following

- It receives some inputs and weights
- Performs some calculations
  - Multiply each input with its associated weight.
  - We add a bias to the sum. The purpose of the bias is to avoid the weighted sum to be 0 even if all the inputs were 0.
  - The sum of the weighted inputs is passed through and activation function to determine the output. The purpose of the linear function is to introduce non-linearity meaning that it enables the neural network to model non-linear relationships between the inputs and the outputs.

Therefore, the output will be determined by the following formula

y = f(b + <sub>i=1</sub>&sum;<sup>n</sup> w <sub>i</sub> x <sub>i</sub>)

where:

- b represents the bias
- f() is the activation function
- w is a weight
- x is an input
- n is the number of inputs being given to the neuron

## Training

Trainig the model is simply a process of determining the best weights to represent the dataset. In supervised learning, where you have a set of input/output examples, the true value is known beforehand.

For each weights, the model is asserted against a loss function to determine how wrong it was on the dataset. The goals of the loss function is to determine how accurate or inaccurate the current model weights predictions are when compared to the ground truth. There are many different options we can choose from, depending on the underlying task.

The ultimate goal of the training process is to update the weights such that the predictions are less wrong, or not wrong at all, best case scenario. This is an iterative process! The key idea we use to update the weights is gradient descent.

## Activaion Functions
