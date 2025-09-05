## Week 2: To demonstrate how to use python and pandas to perform basic analyses of univariate data. 

- It involves analyzing one variable at a time to understand its distribution, patterns, and basic characteristics. 
- The goal is to summarise and find insights from that **single variable** without considering relationships with other variables.

#### Case Study: Univariate data analyses on NHANES data [2015-2016]. 
A. CATEGORICAL SUMMARIES
1. Frequency tables:
- The *value_counts* method can be used to determine the number of times that each distinct value of a variable occurs in a data set. 
- In statistical terminology, this is the "frequency distribution" of the variable or "Mode". 
- The *value_counts* method excludes missing values.

2. Proportions:
- The distribution of the categories of a single variable relative to the total.
- To observe the relative sizes of each category.
- Proportion * 100 = Percentages

B. NUMERICAL SUMMARIES
1. Descriptive statistics:
- The *describe* data frame method to get a set of numerical summaries for a quantitative variable.

2. Measures of central tendency:
- Mean
- Median
- Mode

3. Measures of Spread/Variability
- Standard Deviation
- Range
- Variance

C. Graphical Summaries
1. Histogram : Frequency Distribution
2. Side-by-Side Box Plot: To compare several distributions and measures of spread.
3. Stratification: Divide data into smaller, more uniform subsets, and analyze each of these "strata" on its own (frequency bins/cut-off points)
