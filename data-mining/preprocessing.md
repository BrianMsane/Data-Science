# Data Preprocessing in Data Mining

Data preprocessing is a step that involves transforming raw data so that issues owing to the incompleteness or missing data, inconsistency, and/or appropriate representation of trends are reloved in order to achieve a dataset that is in an understandable format.

It is vital becuase applying data mining algorithms on noisy data would not give quality results as they would fail to identify patterns effectively. Therefore, data preprocessing is important to improve the overall data quality. Duplicate or misshing values many give an incorrect view of the overall statistics of data while outliers and inconsistent data point often would tend to disturb the model's overall learning, leading to false predictions.

It is no secret that the data mining techniques like clustering, classification, regression, and even deep learning models perform better when the data is well prepared. This is why improving data quality through preprocessing is fundamental.

There are several data preprocessing techniques which include:

- **Data cleaning** can be applied to clean the data by filling missing values, smooting the noisy data, resolving inconsistency, and removing outliers. To remove noisy data we can use binning, clustering and many other techniques while regression can be use to smoothen the noise.

- **Data integration** merges data from multiple sources into a coherent data source such as a data warehouse.
- **Data reduction.** can reduce the size by, for instance, aggregating, eliminating redundant features, or clustering.

- **Data transformations** can be applied where data are scaled to fall within a smaller range like 0.0 to 1.0 or -1 to 1. This can improve the accuracy and efficiency of data mining algorithms involving distance measurements.

These techniques are not mutually exclusive; they may work together depending on the data we're working on. For example, data cleaning can involve transformations to correct wrong data such as by transforming data fields into a common format. Data can be transformed through normalization, generalization, and so on.

## Data Quality

Data is said to be of good quality as long as it satisfies the requirements of its intended use. Factors that makeup data quality include accuracy, completeness, consistency, timeliness, believability, and interpretability. Each one of these factors is discussed below.

1. Accuracy
   Accuracy referes to how well the informaiton recorded reflects a real event or object. Data inaccuracy can be caused by faulty data collection instruments or computer erors, purposeful submission of incorrect data values by users, erros in data transmission, inconsitency in maning conventions and input formats, etc.
2. Completeness
   Data is considered complete when all mandatory or necessary features are present. The incompleteness of data can occur due to unavailability of requisite information, equipment malfunction during data collection, unintended deletions, or failure to record history or modifications.
3. Consistency
   If the same information stored and used at multiple instance matches, with or without formatting inconsistencies between various sources or data stores, then the data is consistent. It is quantitatively expressed as the percentage of values that match across the different stored instances.
4. Timeliness
   Timeliness also affects data quality as data is of value only when it is available when needed. If the data is outdated or the corrections are incorporated post evaluations or analysis of datasets, the quality is affected.
5. Believability.
   The believability describes the trust the users have in the data. If the data was at any point found to be rife with errors or inconsistencies, its users will likely harbour reservation when it comes to using the data in the future. As this hinders the effective use of data for intended purpose, believability is also a factor in deciding data quality.
6. Interpretability
   Interpretability of data defines how easy it is to understant teh information present in the dataset and derive meaning from it. The availability of statistical data collection and preprocessing methodologies for the users can affect the interpretability of the dataset.

## Major Tasks in Data Preprocessing

In this section, we look at the major steps involved in data pre-processing, namely: data cleaning, data integration, data reduction, and data transformation.

Data cleaning routines work to clean the data by filling missing values, smoothing noisy data, identifying and removind outliers, and resolving inconsistencies. If users believe the data is dirty, they are unlikely to trust the results of any data mining that has or can be applied. Furthermore, dirty data can cause confusion for the mining procedure resulting in unreliable output. Although most mining routines have some procedures for dealing with incomplete or noisy data, they are not always robust. Instead, they may concetrate on avoiding overfitting data to the function being modeled. Therefeor, a useful preprocessing step is to run your data through some data cleaning routinues.

Supposing that you would like to include data from multiple sources in your analysis. This would involve integrating multiple databases, data cubes, or files (i.e., data integration). Yet some attributes representing a given concept may have different names in different databases, causing inconsistencies and redundacies. For insance, the customer identifucation may be referred to as customer_id in one data source while it is christened cust_id in another; yet they have the same data.

Having a large amount of redundata data may slow down or confuse the knowledge discovery process. Clearly, in addition to data cleaning, steps must be taken to help avoid redundacies during data integration. Typically, data cleaning and data integration are performed as a processing step when preparing data for a data warehouse. Additional data cleaning can be performed to detect and remove redundancies that may have resulted from data integration.

So, now we have integrated data from various source and it is highly possible for us to have a huge dataset which will surely result in a slow data mining process. Now we need to find a way to reduce the size of the dataset without jeopardizind the data mining results.

The solution to that is data reduction. Data reduction obtains a reduced representation of the dataset that is much smaller in volume, yet produces the same, or almost the same, analytical results. Data reduction strategies include dimensionality reuction, and numerosity reduction.

In dimensionality reduction, data encoding schemes are applied so as to obtain a reduced or compressed representation of the original data. Example include data compression techniques (e.g., wavelet transforms and principal component analyis), attribute subset selection (e.g., removing irrelevant attributes), and attribute construction (e.g., where a small set of more useful attributes is derived from the original set).

In numerosity reduction, the data are replaced by alternate, smaller represenations using parametric models (e.g., regression or log-linear models) or non-paramentric models (e.g., histograms, clusters, sampling, or data aggregation).

Assuming you have decided that you would like to use a distance-based mining algorithm for your analysis, such as a neural network, nearest neighbouts, classifiers, or clustering. Such methods provide better results if the data to be analyzed have been normalized, that is, scaled to a smaller range. Your data, for example, contains the attributes age and annual salary. The annual salary attribute usually takes much larger values than age therefore, it the attributes are left unnormalized, the distance measurements taken on annual salary will generally outweight distance measuremnts taken in age. Data discretization and concept hierarcy generation can also be usefult where raw data values for attributes are replaced with ranges or higher conceptaul levels. For example, raw values may be replaced by higher-level concepts such as youth, adult and senior.

Discretization and concept hierachy generation are powerful tools for data mining in that they allow data mining at multiple abstraction levels. Together with normalization, they are forms of data transformation.

In summary, real-world data tend to be dirty, incomplete, and inconsistent so data preprocessing techniques can improve data quality thereby helping improve the accuracy and efficiency of the subsequent data mining steps. Data preporcessing is an importnt step in the knowledge discovery process because quality decisions must be based on quality data.

## Data Cleaning

Data cleaning routines attempt to fill missing values, smooth out noise while identifying outliers and correct inconsistecies in the data.

### Missing Values

Imagine you need to analyze sales and customer data and you note that many tuples have no recorded value or observation for several attributs such as customer income. There are a couple of options to this.

1. Ingore the tuple: This is usually done when hte class label is missing (assuming that the mining class involves classification). This method is not very effective, unless the tuple contains several attributes with missing values. It is especially poor when the percentage of missing values per attribute varies considerably. By ingnoring the tuple, we do not make use of the remaining attribute's values in the tuple whereas such data could be useful to the task at hand.
2. Filling the missing values manually. In general, this approach is time consuming and may not be feasible given a large dataset with many missing values.
3. Use a global constant to fill the missing values. Replace all missing attribute values by the same constant like "Unknown" of infinity. If missing value are replace with this constant, the mining program may instakenly think they form an interesting concept since they all have a common value.
4. Use a measure of central tendency for the attribute (e.g., mean, median, or mode) to fill the missing value. For normal (symmetric) data distribution, the mean can be used, while skewed data should emply the median.
5. Use the attribute mean or median for all samples belonging to the same class as the given tuple: for example, if classifying customers according to credit risk, we may replace the missing value with the mean income value for customers in the same credit risk category as that of the given tuple. If the data distribution for a given class is skewed, the median is a better choice.
6. Use the most probable value to fill in the missing value: This may be determined with regression, inference-based tools using Bayesian formalism, or decision tree induction. For example, using the other customer attributes in your dataset, you may construct a decision tree to predict the missing value for income.

Methods 3 through 6 are bias to the data - the filled-in value may not be correct. Method 6, however, is a popular strategy. In comparison to the other methods, it uses the most information form the present data to predict missing values. By considering the other attributes' values in its estimation of the missing value, there is a greater chance that the relationshiop between the predited attribute's value and the other attribute are preserved.

It is importnat to note that in some cases missing values may not imply an error in the data but simply imply null values. The three main reasons for null values are (1) it is not know, (2) it is not available, and (3) it is not applicable. So, during data collection you may find that either of these cases hold and during data mining we should take this into consideration as opposed to always trying to impute a value, for instance, the mode. Ideally, each attribute should have one or more rules regarding to the null condition. The rules may specify whether or not null are allowed and/or how such values should be handled and transformed. Fields may not be intentionally left blank if they are to be provided in a later set of the business process. Hence, we should try to put constraint in our database design so it disallows null values for such fields.

### Noisy Data

Noise is a random error or variance in a measured variable. Given a numeric variable such as price, how can we smooth out the data to remove the noise?

**Binning**: Binning methods smooth a sorted data value by consulting its "neighbor-hood"; that is values around it. The sorted values are distributed into a number of buckets or bins. Because binning methods consult the neighborhood of values, they perform local smoothing.

**Regression**: Data smoothing can also be done by regression, a technique that conforms data values to a function. Linear regresssion involves finding the best line to fit two attributes so taht one attribute can be used to predict the other. Multiple linear regresssion is an extension of linear regression, where more than two variables are involved and the data are fit to a multidimensional surface.

**Outlier analysis:** outliers maybe detected by clustering, for example similar values are organizes into clusters. Intuitively, values that fall outside the set of clusters may be considered outliers.

Many data smooting methods are also used for data discretization ( a form of data transformation) and data reduction. For example, the binnging techniques described before reduce the number of distinct values per attribute. This acts as a form of data reduction for logic-based datda mining methods such as decision tree induction, which repeatedly makes value comparison on sorted data. Concept hierarchies are a form of data discretization that can also be used for data smoothing. A concept hierarchy for price, for example, may map real pirce values into expensiver, moderately priced, and expensive, thereby reducting the number of data values to be handled in the mining process.
