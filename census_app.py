# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache_data
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame.

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

# Add title on the main page and in the sidebar.
st.title("Census Data Visualization")
st.sidebar.title("Visualisation Selector")
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox("Show Raw Data"):
  st.write(census_df)
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_list = st.sidebar.multiselect("Select the Charts/Plots:", ["Income Group Distribution", "Gender Distribution", "Income vs. Hours per Week", "Gender vs. Hours per Week", "Workclass vs. Income"])

# Display pie plot using matplotlib module and 'st.pyplot()'
if "Income Group Distribution" in plot_list:
    st.subheader("Income Group Distribution")
    income_counts = census_df['income'].value_counts()
    plt.figure(figsize=(9, 6))
    plt.pie(income_counts, labels=income_counts.index, autopct='%1.2f%%')
    plt.title("Income Group Distribution")
    st.pyplot()

if "Gender Distribution" in plot_list:
    st.subheader("Gender Distribution")
    gender_counts = census_df['gender'].value_counts()
    plt.figure(figsize=(8, 5))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.2f%%')
    plt.title("Gender Distribution")
    st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if "Income vs. Hours per Week" in plot_list:
    st.subheader("Income vs. Hours per Week")
    plt.figure(figsize=(9, 6))
    sns.boxplot(x='income', y='hours-per-week', data=census_df)
    plt.title("Income vs. Hours per Week")
    st.pyplot()

if "Gender vs. Hours per Week" in plot_list:
    st.subheader("Gender vs. Hours per Week")
    plt.figure(figsize=(9, 6))
    sns.boxplot(x='gender', y='hours-per-week', data=census_df)
    plt.title("Gender vs. Hours per Week")
    st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()'
if "Workclass vs. Income" in plot_list:
    st.subheader("Workclass vs. Income")
    plt.figure(figsize=(9, 6))
    sns.countplot(x='workclass', hue='income', data=census_df)
    plt.xticks(rotation=45)
    plt.title("Workclass vs. Income")
    st.pyplot()
