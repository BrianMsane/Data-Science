# Measuring Data Similarity and Dissimilarity

In data mining applicaitons like clustering, outliers analysis, and nearest neighbour classification, we often need ways to assess how alike or unablike objects are, in comparison to one another. These applications are called **distance-based applications**. For example, a store may want to search for clusters of customer objects, resulting in groups of customers with similar characteristics. Here the similarity and dissimilarity of objects is needed so we put similar objects in one cluster while dissimilar objects are kept outside of that cluster.

A cluster is a collection of data objects such that the objects within a clusters are similar to one another and dissimilar to the objects in other clusters.

Outlier analysis also employes clustering-based techniques to identify potential outliers as objects that are highly dissimilar to the others. Knowledge of object similarity can also be used in nearest-neighbor classification schemes where a given object is assigned a class label based on its similarity toward the other objects in the model.

The similarity and dissimilarity measures are also called **_measures of proximity_**. They are both related. A similarity measure for two objects i and j will typically return the value 0 if the objects are unalike. The higher the similarity value, the greater the similarity between objects (typically, a value 1 indicates complete similarity between objects; that are identical). A dissimiarity measure, on the other hand, returns the value 0 if the objects are the same (and therefore far from being dissimilar).
