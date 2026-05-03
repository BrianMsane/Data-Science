# Supervised Learning

To introduce supervised learning, let's first delve into its main components. This learning technique requires the data to have inputs, usually denoted as $x^{(i)}$, and outputs, $y^{(i)}$. A pair $(x^{(i)}, y^{(i)})$ is called a training example. To train models for supervised learning, we require a dataset of $n$ examples, $D = {\{x^{(i)}, y^{(i)}\}}^n$. In the training set, the set of all input features is defined as $X$ and the set of all outputs is defined as $Y$. To describe supervised learning formally, our goal is to learn a function $h: X \rightarrow Y$ so that $h(x)$ is a "good" predictor of the corresponding $y$ value. The function $h(x)$ is called a hypothesis.

**Regression problems**: When the target variable we're trying to predict is continuous, $y^{(i)}  \in \mathbb{R}$, we call the learning problem a regression problem. Here, the model $h_\theta$ should also output a real number $h_\theta (x) \in \mathbb{R}$. We define the least squares cost function for the i-th example $(x^{(i)}, y^{(i)})$ as:
$$J^{(i)} (\theta) =  \frac{1}{2}(h_\theta (x^{(i)}) - y^{(i)})^2$$

and define the mean-squared cost function for the entire dataset as:
$$ J(\theta) = \frac{1}{n} \sum_{i=1}^n J^{(i)} (\theta).$$

**Binary classification**: In binary classification, the $Y$ only has two possible classes which are normally encoded as 0 and 1 $y \in \{0, 1\}$. Suppose the inputs $x \in \mathbb{R}^d$. Let $\bar{h}_\theta : \mathbb{R}^d \rightarrow \mathbb{R}$ be a parameterized model. We call the output $\bar{h}_\theta (x) \in \mathbb{R}$ the logit. We use the logistic function $g(\cdot)$ to turn the log $\bar{h}_\theta (x)$ into a probability that $h_\theta(x) \in [0,1]$:

$$
h_\theta(x) = g(\bar{h}_\theta (x)) = 1/1+\exp^{(-\bar{h}_\theta (x))}
$$

We model the conditional probability of $y$ given $\theta$ and $x$ by $P(y=1|x;\theta) = h_\theta(x)$ and $P(y=0|x;\theta) = 1- h_\theta(x)$

**Multi-class classification**: On the other hand, multiclass classification has more than two classes $y \in \{1, 2, \dots, k\}$. Let $\bar{h}_\theta : \mathbb{R}^d \rightarrow \mathbb{R}^k$ be a parameterized model. We call the outputs $\bar{h}_\theta(x) \in \mathbb{R}^k$ the logits. We use the softmax function to turn the logits into a probability vector with non-negative entries that sum up to 1:

$$
P(y=j|x;\theta) = \frac{\exp(\bar{h}_\theta(x)_j)}{\sum_{s=1}^k \exp(\bar{h}_\theta(x)_s)}
$$

where $\bar{h}_\theta(x)_s$ denotes the s-th coordinate of $\bar{h}_\theta(x)$.
