# Neural Networks

Deep learning uses neurons as the basic building block!

## Perceptron

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

## Training - Forward Pass

Trainig the model is simply a process of determining the best weights to represent the dataset. In supervised learning, where you have a set of input/output examples, the true value is known beforehand.

For each weights, the model is asserted against a loss function to determine how wrong it was on the dataset. The goals of the loss function is to determine how accurate or inaccurate the current model weights predictions are when compared to the ground truth. There are many different options we can choose from, depending on the underlying task.

The ultimate goal of the training process is to update the weights such that the predictions are less wrong, or not wrong at all, best case scenario. This is an iterative process! The key idea we use to update the weights is gradient descent.

## Activation Functions

As mentioned, each node computes the sum of weight and inputs and then add the bias, the output of that is passed through an activation function. Without activation functions, neural networks would be restricted to modeling only linear relationships between inputs and outputs so they introduce non-linearity which allows NN to learn highly complex mappings between inputs and outputs.

Practically, most real-world data is non-linear so we need to ensure that NN are flexible enough to model such data through the use of activation functions. Also, choosing the right activation function is very important as each activation function has unique properties and is suitable for certain use cases. Using the right function leads to faster training and better performance.

- Linear: regression output
- Sigmoid: ideal for binary classification
- Softmax: ideal for multi-class classificaton
- Hyperbolic tangent: efficient training with normalized data; when used in hidden layers
- Rectified linear : helps overcome the vanishing gradient problem

Different types of activation functions

1. Linear
   This is the simplest activaton function which is defined by this formula f(x) = x. This means that is simply returns x as the output - projects what it receives. The main use cas of this function is in the output layer of a NN used for regression. This is because this activation function does not transform the output so the actual predicted value will be returned. In regression, we want to return a continous, numerical value.

   It is rarely used in hidden layers and this is becuase it does not provide any non-linearity yet the point of having these layers is to deeply learn the non-linear behaviour of the data so using this activation function is a restriction of having to learn only linear mappings.

2. Sigmoid
   This is a smooth functoin defined by this formula f(x) = 1 / (1+ e ^-x). What it does is that it takes the input and squash it to a value between 0 and 1. It has an S shape that asymptotes 0 for large negative numbers and 1 for large positive numbers.

   The outputs can be easily interpreted as probabilities, which makes it suitable for binary classification problems. However, sigmoid units suffer from the vanishing gradient problem that hampers learning in deep neural networks. As the input value become significantly positive or negative, the function saturates at 0 or 1. In these regions, the gradient is very close to 0 and this results in very small changes in the weights during backpropagations which makes the learning tremendously slow or even halts it. This is referred to the vanishing gradient problem in NN.

   The main use is in the output layer of an binary classification models. It squashes the output to a probability value between 0 and 1 which can be interpreted as the probability of the input belonging to a particular class.

3. Hyperbolic Tangent (tanh)
   The activation function is defined as f(x) = (e^x -e^-x)/(e^x +e^-x). It outputs a value between -1 and 1. This means taht it can deal with negative values more effectively than the sigmoid function, which has a range of 0 and 1.

   This function is zero-centered, which means that its ouput is symmetric around the origin - of the coordinate system. This is often considered as an advantage because it can help the learning algorithm converge faster. More like the sigmoid function, it still suffers the vanishing gradient problem.

   During backpropagation, the gradients can become very small - close to 0. This issue is particulary problematic for deep networks with many layers; the gradient of the loss funciton may become too small to make significant changes in the weights during hte training as they propage back to the initial layers.

   It is frequently used in the hidden layer. Because of its zero-centered nature, when the data is also normalized to have mean 0, it can result in more efficient training.

4. Rectified Linear Unit (ReLU)
   Defined as f(x) = max(0, x). It thresholds the input at zero, outputing zero for negative values and the input itself - untransformed, for positive values. You can also say that it acts as the linear activation function for positive inputs. It allows the gradient to pass through unchanged during propagation. This property is crucial in mitigating the vanishing gradient problem.

   Since it outputs 0 for all negative inputs, it naturally leads to sparse activations; at any time, only a subset of neurons are activated, leading to more efficient computations

5. Softmax
   The softmax, also known as the exponential function, is particulaly useful within the context of multi-class classification problems. It operates on a vector, often referred to as the logits, which represents the raw prediction or scores for each class computed by the previous layers on the NN.

   For the input vector x with element x1, x2, ..., xc, the softmax function is defined as f(xi) = e^xi / &sum;j e^xj. The output is a probability distribution that sums up to 1. Each element of the output represents the probability that the input belongs to a particular class.

   The use of the exponential function ensures that all the output values are non-negative and this is crucial because probabilities cannot be negative. The probabilities produced by the softmax function can be interpreted as the confidence scores for each class, providing insight into the model's certainty about the predictions.

   Softmax amplifies differences in the input vector. Even small differences in the input values can lead to substantial differences in the output probabilities, with the highest input value(s) tending to dominate in the resulting probability distribution. Because it amplifies differences, it can be sensitive to outliers or extreme values.

## Gradient Descent, its Varients, and Other Optimizers

- Stochastic Gradient Descent
- Mini-batch GD
- Other Optimizers
  - Adam

## Backpropagation

Intuitively, the process of backpropagation can be defined as follows.
