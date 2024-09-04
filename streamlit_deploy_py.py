import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

# Set page config
st.set_page_config(page_title="HDB Resale Prices Dashboard", layout="wide")

# Title of the dashboard
st.title("HDB Resale Prices Dashboard")

# Load dataset
# @st.cache
# def load_data():
#     data = pd.read_csv('/content/drive/MyDrive/Data Sprint/data/model2.csv')
#     return data


# df = load_data()

from pycaret.regression import *
model = load_model('best_model')

# Display the dataset
st.subheader("Dataset Overview")
st.write(df.head())

# Sidebar filters
st.sidebar.header("Filters")

# # Filter by town
# towns = df['region'].unique()
# selected_town = st.sidebar.multiselect("Select Region(s):", regions, default=regions)

# Filter by flat type
flat_types = df['flat_type'].unique()
selected_flat_type = st.sidebar.multiselect("Select Flat Type(s):", flat_types, default=flat_types)

# # Filter by year
# df['year'] = pd.to_datetime(df['month']).dt.year
# years = df['year'].unique()
# selected_year = st.sidebar.slider("Select Year Range:", int(years.min()), int(years.max()), (int(years.min()), int(years.max())))

# # Apply filters
# filtered_df = df[
#     (df['region'].isin(selected_town)) &
#     (df['flat_type'].isin(selected_flat_type)) &
#     (df['year'].between(selected_year[0], selected_year[1]))

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Visualization
st.subheader("Visualizations")

# # Distribution of Resale Prices
# st.markdown("### Distribution of Resale Prices")
# fig, ax = plt.subplots()
# sns.histplot(filtered_df['resale_price'], bins=30, kde=True, ax=ax)
# ax.set_title('Distribution of Resale Prices')
# ax.set_xlabel('Resale Price')
# ax.set_ylabel('Frequency')
# st.pyplot(fig)

# Average Resale Price by Town
st.markdown("### Average Resale Price by Region")
avg_price_by_town = filtered_df.groupby('region')['resale_price'].mean().sort_values()
fig, ax = plt.subplots(figsize=(10, 8))
avg_price_by_town.plot(kind='barh', ax=ax)
ax.set_title('Average Resale Price by region')
ax.set_xlabel('Average Resale Price')
ax.set_ylabel('region')
st.pyplot(fig)

# Resale Price Trend over Time
st.markdown("### Resale Price Trend over Time")
avg_price_by_month = filtered_df.groupby('month')['resale_price'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
avg_price_by_month.plot(ax=ax)
ax.set_title('Resale Price Trend Over Time')
ax.set_xlabel('Month')
ax.set_ylabel('Average Resale Price')
st.pyplot(fig)

# Download filtered data
st.subheader("Download Filtered Data")
st.markdown("You can download the filtered data below:")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(label="Download CSV", data=csv, file_name='filtered_hdb_resale_prices.csv', mime='text/csv')

# Run the app
if __name__ == '__main__':
    st.run()
