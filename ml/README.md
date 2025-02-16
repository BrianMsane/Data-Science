# The Pipeline of a Machine Learning Project

1. Gathering Data
2. Finding the space of possible solutions. Generate hypothesis
3. Characterizing the objectives (what makes a good solution)
4. Finding the learning algorithm
5. Running the algorithm
6. Validation of the results

In all these steps, except for the fifthe - running the algorithm, have to be done by a human rather than a machine.

The third step introduces the concept of a loss function which can be generally viewed as the difference between the prediction and the actual data values. The more we make mistakes, the higher the loss function and the opposite is true for matching prediction. Typically, we opt for the lowest loss function possible and a solution which gives us that is then regarded as a good solution. We usually employ optimization techniques to find the best solution; this is usually done at the process of running the chosen algorithm.

## Training set error vs testing set error

## Types of ML Techniques

- Supervised Learning.

  Here, we have a dataset which has the input features, or attributes, and the known outputs and the main idea is to learn the relationship between the inputs and the output. The inputs can be denoted as X and the outupt as Y. Upon having the data, we need to train the model in a supervised manner. This manner guides the model to predict the known output. During this process, the model learns the relationship.

  At inference stage, where we make use of the trained model, we are going to have only the input attributes and the goal is to predict the unknown output.

  The main tasks under supervised learning are:

  - Classification

    - Binary classification. Two possible output categories.
    - Multi-class classification. Multiple, more than two, output possibilities.

  - Regression

- Unsupervised learning.

  This does not involve learning a funciton from inputs to outpus base on a set on input-output pairs. Instead, we are given a dataset of only attributes and we're expected to find the patterns based on the given attributes. These patterns distinguish the data.

  The main tasks under unsupervised learning are:

  - Clustering

- Semi-supervised learning.
- Reinforcement learning.
