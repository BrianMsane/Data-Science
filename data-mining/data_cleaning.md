# Data Cleaning

Raw data in real-file scenario has the tendency of being incomplete, noisy, and inconsistent. So, data cleaning routines attempt to fill missing values, smooth out noise while identifying outliers and correct inconsistecies in the data.

## Missing Values

Imagine you need to analyze sales and customer data and you note that many tuples have no recorded value or observation for several attributs such as customer income. There are a couple of options to this.

1. **Ingore the tuple:** This is usually done when the class label is missing (assuming that the mining class involves classification). This method is not very effective, unless the tuple contains several attributes with missing values. It is especially poor when the percentage of missing values per attribute varies considerably. By ingnoring the tuple, we do not make use of the remaining attributes' values in the tuple whereas such data could be useful to the task at hand; that is, we're losing some useful information.

2. **Filling the missing values manually**. In general, this approach is time consuming and may not be feasible given a large dataset with many missing values. But, if the missing values are filled by a domain expert, there is a high chance that they become accurate be of good quality.

3. Use a **global constant** to fill the missing values. Replace all missing attribute values by the same constant like "Unknown" or infinity ♾️. If missing value are replace with this constant, the mining program may _mistakenly think they form an interesting concept_ since they all have a common value.

4. Use a **measure of central tendency** for the attribute (e.g., mean, median, or mode) to fill the missing value. For normal (symmetric) data distribution, the mean can be used, while skewed data should emply the median. Be mindful of the attribute type as well, for instance, it makes no sense to use the mean for nominal, binary and ordinal attributes' missing values even if these are represented numerically.

5. Use the attribute mean or median for all samples belonging to the same class as the given tuple: for example, if classifying customers according to credit risk, we may replace the missing value with the mean income value for customers in the same credit risk category as that of the given tuple. If the data distribution for a given class is skewed, the median is a better choice.

6. Use the **most probable value** to fill in the missing value: This may be determined with _regression, inference-based tools using Bayesian formalism, or decision tree induction_. For example, using the other customer attributes in your dataset, you may construct a decision tree to predict the missing value for income.

Methods 3 through 6 are bias to the data - the filled-in value may not be correct. Method 6, however, is a popular strategy. In comparison to the other methods, it uses the _most information form the present data to predict missing values_. By considering the other attributes' values in its estimation of the missing value, there is a greater chance that the relationship between the predited attribute's value and the other attribute are preserved.

It is importnat to note that in some cases missing values may not imply an error in the data but simply imply null values. The three main reasons for null values are (1) it is not know, (2) it is not available, and (3) it is not applicable. So, during data collection you may find that either of these cases hold and during data mining we should take this into consideration as opposed to always trying to impute a value, for instance, the mode. Ideally, each attribute should have one or more rules regarding to the null condition. The rules may specify whether or not null are allowed and/or how such values should be handled and transformed. Fields may not be intentionally left blank if they are to be provided in a later set of the business process. Hence, we should try to put constraint in our database design so it disallows null values for such fields.

### Noisy Data

Noise is a random error or variance in a measured variable. Given a numeric variable such as price, how can we smooth out the data to remove the noise?

**Binning**: Binning methods smooth a sorted data value by consulting its "neighbor-hood"; that is values around it. The sorted values are distributed into a number of buckets or bins. Because binning methods consult the neighborhood of values, they perform local smoothing.

**Regression**: Data smoothing can also be done by regression, a technique that conforms data values to a function. Linear regresssion involves finding the best line to fit two attributes so taht one attribute can be used to predict the other. Multiple linear regresssion is an extension of linear regression, where more than two variables are involved and the data are fit to a multidimensional surface.

**Outlier analysis:** outliers maybe detected by clustering, for example similar values are organizes into clusters. Intuitively, values that fall outside the set of clusters may be considered outliers.

Many data smooting methods are also used for data discretization ( a form of data transformation) and data reduction. For example, the binnging techniques described before reduce the number of distinct values per attribute. This acts as a form of data reduction for logic-based datda mining methods such as decision tree induction, which repeatedly makes value comparison on sorted data. Concept hierarchies are a form of data discretization that can also be used for data smoothing. A concept hierarchy for price, for example, may map real pirce values into expensiver, moderately priced, and expensive, thereby reducting the number of data values to be handled in the mining process.
