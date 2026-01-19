Kenyan Maize Dataset Analysis
Objective
The main objective of this notebook is to explore and understand the 'Kenyan Maize Dataset' to potentially identify factors influencing maize yield.

Dataset Description
The dataset used in this notebook is the 'Kenyan Maize Dataset', loaded from the file 'maize.csv'. It contains information related to maize yield in Kenya over several years. The columns in the dataset include:

Item: The crop item (Maize)
Year: The year of observation
hg/ha_yield: Maize yield in hectograms per hectare
average_rain_fall_mm_per_year: Average annual rainfall in millimeters
pesticides_tonnes: Amount of pesticides used in tonnes
avg_temp: Average temperature
Area: The geographical area (Kenya)
Notebook Steps
Sequence of Actions Performed in the Notebook:

Data Loading: The dataset was loaded into a pandas DataFrame named df from the CSV file 'maize.csv'.

Initial Data Inspection:

The first few rows of the DataFrame were displayed using df.head() to get a preliminary look at the data.
The column names were checked using df.columns.
Information about the DataFrame, including data types and non-null counts, was examined using df.info(). This confirmed that there were no missing values in the dataset.
Descriptive statistics (count, mean, std, min, max, quartiles) for the numerical columns were generated using df.describe().
The shape of the DataFrame (number of rows and columns) was checked using df.shape.
Data Cleaning - Column Removal: The 'Unnamed: 0' column, which appeared to be an index column and not relevant for the analysis, was removed from the DataFrame.

Data Cleaning - Column Renaming: Although not permanently saved to the DataFrame, a step was taken to rename some columns for better readability ('average_rain_fall_mm_per_year' to 'Average_Rain_Fall_MM_PER_YEAR', 'pesticides_tonnes' to 'Pesticides_Tonnes', 'avg_temp' to 'Avg_Temp') using df.rename().

Data Cleaning - Duplicate Check: Duplicate rows in the DataFrame were identified using df.duplicated(). The output indicated no duplicate rows.

These steps covered the initial loading, basic inspection, and some preliminary cleaning of the dataset before any deeper analysis or modeling.

Key Findings
Key Findings from Initial Data Analysis:

Based on the initial exploratory data analysis, the following significant observations and patterns were derived from the dataset:

Numerical Column Summary (df.describe()):

hg/ha_yield: The maize yield varies significantly, with a minimum of 849 hg/ha and a maximum of 207556 hg/ha. The mean yield is around 36310 hg/ha, with a standard deviation of 27456, indicating a wide distribution in yield values.
average_rain_fall_mm_per_year: Rainfall also shows considerable variation, ranging from 51 mm to 3240 mm annually. The mean rainfall is approximately 1098 mm.
pesticides_tonnes: Pesticide usage varies greatly, from a minimum of 0.04 tonnes to a maximum of 367778 tonnes. The mean usage is around 32766 tonnes, with a large standard deviation (54088), suggesting a highly skewed distribution or outliers in pesticide application.
avg_temp: Average temperature has a smaller range compared to yield, rainfall, and pesticides, varying from 1.61°C to 30.65°C. The mean temperature is around 19.93°C.
Year: The data spans from 1990 to 2013.
Data Quality (df.info(), Duplicate Check):

df.info() revealed that there are no missing values across all columns, which is excellent for data quality and means no imputation or handling of missing data is required at this stage.
The duplicate check (df.duplicated()) confirmed that there are no duplicate rows in the dataset, indicating the data is unique and consistent in this regard.
Overall, the dataset appears to be clean with no missing values or duplicates. The numerical features, particularly 'hg/ha_yield', 'average_rain_fall_mm_per_year', and 'pesticides_tonnes', exhibit significant variability, which could be important factors influencing maize yield. The wide range in pesticide usage might warrant further investigation into its distribution and potential impact on yield.