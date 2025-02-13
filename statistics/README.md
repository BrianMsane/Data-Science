# Statistics

- Types of data
- Population and sampling
- Sampling methods or techniques
- Types of statistics
- Measures of central tendency
- Measures of variance
- Outliers
- Covariance

## Distributions

- Normal distribution
- Binomial distribution
- Uniform distribution
- Bernoulli's distribution
- Poisson distribution
- Exponential distribution
- Relation between the distribution

## Hypothesis and computational methods

- Null hypothesis, p-value
- One tailed and two tailed test
- Type 1 and 2 errors
- Parametric tests
  - T-test
  - ANOVA test
  - Pearson's R test
- Non-parametric tests
  - Mann-Whitenty U test
  - Wilcoxon Signed Rank test
  - Krushal-Wallis H test
  - Friedman test
  - Spearson's test (rho)
- Chi-squared test

## Correlation and regression

- Introduction to regression
- Types of regression
- Co-relation

## Mean

The mean is the arithmetic average of a set of numbers and represents the central value of the dataset. It is computed by summing all values and dividing by their count. The mean is a foundational measure in statistics because it incorporates every value in the dataset, making it sensitive to changes in any observation. However, because it uses all values, it can be affected by outliers or extreme values. In many statistical applications and data science models, the mean is used to summarize data and serve as a reference point for further analysis.

## Mode

The mode is the value that appears most frequently in a dataset. Unlike the mean and median, which provide measures of central tendency, the mode gives insight into the most common or popular value in the distribution. This characteristic makes it particularly useful in categorical data analysis, where numerical averages might not be meaningful. A dataset may be unimodal (one mode), bimodal (two modes), or multimodal (more than two modes), which can reveal the underlying structure or subgroups within the data.

## Median

The median is the middle value of an ordered dataset and divides the data into two equal halves. As a measure of central tendency, it is more robust against outliers than the mean because it is solely based on the ordering of values rather than their magnitude. In skewed distributions, where extreme values might distort the mean, the median often provides a more accurate representation of the central location. This quality makes it a preferred measure in many practical applications, especially when dealing with income, property prices, or other data that may not be symmetrically distributed.

## Variance

Variance quantifies the spread or dispersion within a dataset by measuring how far each data point lies from the mean. It captures the degree of variability, offering insights into how much the individual values differ from the central tendency. Higher variance indicates that the data points are spread out over a wider range, while lower variance means they are clustered closely around the mean. This measure is critical in various fields, from risk assessment in finance to error analysis in scientific research. Conceptually, variance is all about understanding the data’s consistency and reliability.

## Standard Deviation

Standard deviation is the square root of the variance and provides a measure of dispersion that is expressed in the same units as the original data. It reflects how spread out the data is around the mean, but it is generally more interpretable for most applications. A small standard deviation indicates that the data points tend to be very close to the mean, suggesting high consistency, whereas a large standard deviation shows that the data are more spread out, hinting at higher variability or uncertainty. It is widely used in fields ranging from quality control to finance and research to set confidence intervals and assess risk.

## Z-scores

A z-score tells you how many standard deviations a particular value is away from the mean of its distribution. It standardizes individual data points by expressing how far they are from the mean on a scale where the mean is zero and the standard deviation is one. This transformation makes it possible to compare values from different distributions on a common scale, enabling meaningful comparisons even when the original units differ. Z-scores are crucial in detecting outliers—values with a high or low z-score may indicate an anomaly or a significant deviation from expected behavior. Additionally, this standardization underpins many inferential statistical techniques, such as hypothesis testing and regression analysis.
