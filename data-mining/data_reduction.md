# Data Reduction

Data reduction techniques can be applied to obtain a reduced representation of the datasets that is much smaller in volume, yet closely maintains the integrity of the original data. That is, mining on teh reduced dataset should be more efficient yet produce the same or almost the same analytical results. The strategies which are often used inlcude dimensionality reduction, numerosity reduction, and data compression.

Dimensionality reduction is the process of reducing the number of random variables or attributes under consideration. Dimensionality reduction methods include wavelet transforms and principal component analysis which transforms or project teh original data onto a smaller space. Attribute subset selection is a method of dimensionality reduction in which irrelevant, weakly relevant, or redundant attributes are detected and removed.

Numeriosity reduction techniques replaces the originaly data volument by alternative, smaller forms of data representations. These techniques may be parametric or non-parametric. For parametric methods, a models is used to estimate the data, so that typically only hte data parametrer need to be stored, instead of the actual data. (Outliers may also be stored). Regression and log-linear models are examples. Non-parametric methods for storing reduced representations of the data include histograms, clustering, sampling, and cube aggregation.

In data compression, transformations are applied so as to obtain a reduced or "compresses" representation of the original data. If the original data can be reconstructed from the compressed data without any informationloss, the data reduction is called lossless. If, instead, we can reconstruct only an approximation of the original data, then the data reduction is called lossy. There are several lossless algorithms for string compression; however, they typically allow only limited data manipulation. Dimensionality reduction and numerosity reduction techniques can also be considered forms of data compression.

## Wavelet Transfroms

## Principal Component Analysis

PCA is a methods of dimensionality reduction. Suppose that the data consist of tuples or data vectors described by n attributes of dimensions. PCA searches for k n-dimensional orthogonal vectores that can be be sued to represent the data, where k <= n. The original data are thus projected onto a much smaller space, resulting in dimensionality reduction. Unlike attributes subset selection, which reduces the size by retaining a subset of the inintal set of attributes, PCA "combines" the essence of attributes by creating an alternative, smaller set of variables. The initial data can be projected ont this smaller set. PCA often reveals relationships that wer not previously suspected and thereby allows intepretations that would not ordinarily result.

The baisc procedure is as follows:\

- The input data are normalized, so taht each attribute falls within the same range. This step helps ensure that attributes with large domains will not dominate other attributes with smaller domains.

- PCA computes k othonormal vectors taht provide the basis for the normalized input data. These are unit vectors that each point in a direction perpendicular to the others. These vectors are referred to as principal components. The input data are linear combination of the principal components.

- The principal components are sorted in order of decreasing "significance" or strength. The principal components essentially serve as a new set of axes for the data, providing important information about variance. That is, the sorted axes are such that the first axis show most variance among the data, the second axis show the highest variance and so on.

- Because the components are sorted in decreasing order of significance, the size of the data can be reduced by eliminating the weaker components, that is, those with low variance. Using the strongest principal components, it should be possible to reconstruct a good approximation of the original data.

PCA can be applied to ordered and unordered attributes, and can handle sparse data and skewed data. Multidimensional data of two dimensions can be handled by reducing the problem to two dimensions. Pricipal components may be used as inputs to multiple regression and cluster analysis. In comparison to wavelet transforms, PCA tends to be better at handling sparse data, wherease wavelet transforms are more suitable for data of high dimensionality.

## Attribute Subset Selection

Datasets for analysis may contain hundreds of attributes, many of which may be irrelevant to the mining task or redundant. For example, it the task is to classify customers based on whether or not they are likely to purchase a popular new item when notified of a sa.e, attributes such as the customer's telephone number are likely to be irrelevant. Although it may be possible for a domain expert to pick out some of the useful attributes, this can be difficult and time-consuming, especially when the data's behavior is not well known. Leaving out relevant attribute or keeping irrelevant attributes may be dtrimental, causing confusion to the mining algorithm employed. This can result in discovered patters of poor quality. In addition, the added volume of irrelevant attributes can slow down the minign process.

Attributes subset selection reduces the sizes of the data by removing irrelevant or redundant dimensions. The goal is to find a minimum set of attributes such that the resulting probability distribution of the data classes is as close as possible to the original distribution obtained using all attributes. Mining on a reduced set of attributes has an additional benefit: it reduces teh number of attributes appearing in the discovered patterns, helpgin to make the patterns easier to understand.

For n attributes, there are 2^n possible subsets. An exhaustive search for the optimal subset of attribute can be prohibitively expensive, especially as n and the number of data classes increase. Therefore, heuristic methods that explore a reduced search space are commonly used for attribute subset selection. These methods are typically greedy in that, while searching through attribute space, they always make what looks to be the best choice at the time. Their strategy is to make a locally optimal choice in the hope that this will lead to a globally optimal solution. Such greedy methods are effective in practice and may come close to estimating an optimal solution.

The best and worst attributes are typically determined using tests of statistical significance, which assumes taht the attributes are independent of each other. Many other attribute evaluation measures can be sued such as the information gain measure used in building decision trees for classification.

Basic heuristic methods of attribute subset selection include the following techniques.

- Stepwise forward selection. The procedure starts with an empty set of attributes as the reduced set. The best on teh original attributes is determined and added to the reduced set. At each subequent iteration, the best of the reamining orignal attributes is added to the set.
- Stepwise backward elimination. The procedure starts with the the full set of attributes. At each step, it removes the worst attribute remaining in the set.
- Combination of forward selection and backward elimination. The stepwise forward selection and backward elimination methods can be combined so that at each step, the procedure selects the best attributes and removes the worst from among the remaining attributes.
- Decision tree induction. Decision tree algorithms (e.g., ID3, C4.5, and CART) were originally intended for classification. Decision tree induction constructs a flowchart-like structure where each internal (non-leaf) node denotes a test on an attribute, each branch corresponds to an outcome of the test, and each external (leaf) node denotes a class prediction. At each node, the algorithm chooses the best attribute to partition the data into individual classes.

When decision tree induction is used for attribute subset selection, a tree is constructed from the given data. All attributes that do not appear in the tree are assumed irrelevant. The set of attributes appearing in the tree form the reduced subset of attributes.

The stopping criteria for the methods may vary. The procedure may employ a threshold on the measure used to determing when to stop the attribute selection process.

IN some cases, we may want to create new attributes based on others. Such attribute construction can help improve accuracy and understanding of structure in high-dimensional data. For example, we may wish to add a new attribute area based on the attributes height and width. By combining attributes, attribute construction can discover missing information about the relationship between data attributes that can be useful for knowledge discovery.

## Regression and Log-linear Models: Parametric Data Reduction

Regression and log-linear models can be used to approximate the given data. In linear regression, the data can be modeled to fit a straight line. For example, a random variable, y (called a response variable), can be modeled as a linear function or another random variable, x (called the predictor variable), with and equation y= mx + b where the variance of y is assumed to be constant. In the context of data mining, x and y are numeric database attributes. The coefficients, w and b (called regression coefficient), specify the slope of the line and the y-intercept, respectively. The coefficients can be solved for by the method of least squares, which minimizes the error between the actual line separating the data and the estimate of the line. Multiple linear regression is an extetion of linear regression whic allowsa response variable to be modeled as a linear function of two or more predictor variables.

Log-linear models approximate discrete multidimensional probability distributions. Given a set of tuples in n dimension, we can consider each tuple as a point in an n-dimensioal space. Log-linear models can be used to estimate the probability of each point in a multidimensional space for a set of discretized attributes, based on a smaller subset of dimensional combinations. This allows a higher-dimensional data space to be constructed from lower-dimensional spaces. Log-linear models are therefore also useful for dimensionality reduction (since the lower-dimensional points together typically occupy less space than the original data points) and data smoothing (since aggregate estimates in teh lower-dimensional space are less subject to sampling variations than the estimates in the higher-dimensional space).

Regression and log-linear models can both be used on sparse data, although their application may be limited. While both methods can handle skewed data, regression does exceptionally well. Regression can be computationally intensive when applied to high-dimensional data, whereas log-linear models show good scalability up to 10 or so dimensions.

## Clustering

## Data Cube Aggregation
