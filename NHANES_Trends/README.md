# Statistics with Python
NHANES project demonstrates the application of statistical analysis concepts using Python in Visual Studio Code. It showcases how to analyze, visualize, and model data to answer research questions in healthcare datasets.

#### Features
- Utilize Python packages and libraries to create and interpret data visualizations.
- Apply and interpret inferential statistical procedures on real datasets.
- Implement statistical modeling techniques, including:
    - Linear and logistic regression
    - Linear models
    - Multilevel models
    - Bayesian inference techniques
- Conduct data-driven research and answer research questions using statistical methods.

#### Project Structure
The project is organized into three main parts:
1. Understanding and Visualizing Data – Explore datasets and create insightful visualizations.
2. Inferential Statistical Analysis – Apply hypothesis testing and inferential procedures to draw conclusions from data.
3. Fitting Statistical Models to Data – Build and interpret various statistical models to explain and predict outcomes.

#### Learning Context
This project is based on the [Statistics with Python Specialization](https://www.coursera.org/specializations/statistics-with-python) offered by the University of Michigan on Coursera. It reflects practical exercises and applications from the course.

### Dataset: NHANES
- This project uses data from the National Health and Nutrition Examination Survey (NHANES), a program of studies conducted by the National Center for Health Statistics (NCHS). The dataset provides a representative sample of the U.S. population, making it widely used for public health and epidemiological research.

- NHANES data and documentation are freely available from the [CDC website](https://wwwn.cdc.gov/nchs/nhanes/).

- NHANES combines:
    1. Interviews (demographic, socioeconomic, dietary, and health-related questions)
    2. Physical examinations (medical, dental, physiological measurements, laboratory tests)

- This project uses data from the National Health and Nutrition Examination Survey (NHANES) 2015–2016, which includes information from approximately 5,600 participants.

## PART 1: Understanding and Visualizing Data
This section demonstrates how to use *pandas* to perform basic analyses, with a focus on **univariate data**. The goal is to understand the distribution, patterns, and key characteristics of a single variable.

#### A. Categorical Summaries

1. Frequency tables:
- Use *value_counts()* to determine how many times each distinct value occurs in the dataset.
- This represents the frequency distribution of the variable (statistically linked to the mode).
- Note: Missing values are excluded by default.

2. Proportions:
- Distribution of categories of a single variable relative to the total.
- Helps in observing the relative sizes of each category.
- Multiplying proportions by 100 gives percentages.

#### B. Numerical Summaries

1. Descriptive statistics:
- Use the *describe()* method to obtain a set of numerical summaries for quantitative variables.

2. Measures of central tendency:
- Mean
- Median
- Mode

3. Measures of spread / variability:
- Standard deviation
- Range
- Variance

#### C. Graphical Summaries 
- Use the *matplotlib* and *seaborn* libraries for visualisation.
- **Histogram**: Displays the frequency distribution of a variable.
- **Side-by-side box plots**: Compare multiple distributions and their spread.
- **Stratification**: Divide data into smaller, more uniform subsets (“strata”) and analyze each separately (e.g., frequency bins or cut-off points).

## PART 2: Inferential Statistical Analysis


