import streamlit as st
import pandas as pd

# Load data to get structure (optional if loading directly from the CSV file)
data = pd.read_csv('X_train_transformed.csv')

# Create a dictionary to map dummy variable groups to their base inputs
dummy_mappings = {
    'region': ['Central', 'East', 'North', 'Others', 'West'],
    'flat_model': ['2-room', 'Adjoined flat', 'Apartment', 'DBSS', 'Improved', 
                   'Improved-Maisonette', 'Maisonette', 'Model A', 'Model A-Maisonette', 
                   'Model A2', 'Multi Generation', 'New Generation', 
                   'Premium Apartment', 'Premium Apartment Loft', 
                   'Premium Maisonette', 'Simplified', 'Standard', 'Terrace', 
                   'Type S1', 'Type S2'],
    'storey_category': ['1-5', '6-10', '11-15', '16-20', '21-25', 
                        '26-30', '31-35', '36-40', '41-45', '46-50', '>50']
}

# Define user inputs for the non-dummy columns
tranc_year_month = st.text_input('Transaction Year-Month', '2024-01')
town = st.text_input('Town', 'Example Town')
flat_type = st.selectbox('Flat Type', ['1 Room', '2 Room', '3 Room', '4 Room', '5 Room', 'Executive'])
hdb_age = st.number_input('HDB Age (years)', min_value=0, max_value=99, value=20)
total_dwelling_units = st.number_input('Total Dwelling Units', min_value=1, value=100)
remaining_lease = st.number_input('Remaining Lease (years)', min_value=1, value=60)
amenities_1km = st.number_input('Amenities within 1km', min_value=0, value=5)
pri_dist_vac = st.number_input('Primary School Distance (Vacancy)', min_value=0, value=10)

# Define user inputs for the consolidated dummy variables
region = st.selectbox('Region', dummy_mappings['region'])
flat_model = st.selectbox('Flat Model', dummy_mappings['flat_model'])
storey_category = st.selectbox('Storey Category', dummy_mappings['storey_category'])

# When the user submits the form, you can collect all inputs and process further
if st.button('Submit'):
    user_input = {
        'Tranc_YearMonth': tranc_year_month,
        'town': town,
        'flat_type': flat_type,
        'hdb_age': hdb_age,
        'total_dwelling_units': total_dwelling_units,
        'remaining_lease': remaining_lease,
        'amenities_1km': amenities_1km,
        'pri_dist_vac': pri_dist_vac,
        'region': region,
        'flat_model': flat_model,
        'storey_category': storey_category
    }

    # Display or further process the user input
    st.write("User Input:", user_input)
