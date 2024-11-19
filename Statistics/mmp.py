# Exercise: Median, Mean, Percentile
#* Use this air bnb new york city data set and remove outliers using percentile based on price per night for a given apartment/home. You can use suitable upper and lower limits on percentile based on your intuition. Your goal is to come up with new pandas dataframe that doesn't have the outliers present in it. https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

import pandas as pd

# Update this path to match your local file path
file_path = "C:/Users/USER/Desktop/MY_ML_JOURNEY/Statistics/AB_NYC_2019.csv"
data = pd.read_csv(file_path)

# Calculate the 1st and 99th percentiles for the `price` column
lower_percentile = data['price'].quantile(0.01)
upper_percentile = data['price'].quantile(0.99)

# Filter the data to remove outliers based on these percentiles
filtered_data = data[(data['price'] >= lower_percentile) & (data['price'] <= upper_percentile)]

# Display summary statistics for the filtered data to confirm outliers are removed
print("Original Price Stats:")
print(data['price'].describe())
print("\nFiltered Price Stats:")
print(filtered_data['price'].describe())

# Save the cleaned dataset to a new CSV file if needed
filtered_data.to_csv("C:/Users/USER/Desktop/MY_ML_JOURNEY/Statistics/cleaned_AB_NYC_2019.csv", index=False)
