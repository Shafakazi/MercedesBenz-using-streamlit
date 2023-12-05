import streamlit as st
import pandas as pd

data = {
    'Model': ['A-class','C-Class', 'E-Class', 'S-Class', 'GLA', 'GLC', 'GLE', 'GLS', 'EQA', 'EQB', 'EQC', 'AMG-GT', 'AMG-GT4', 'AMG ONE', 'Sprinter', 'Vito', 'Citan', 'Actros', 'Arocs', 'Econic', 'Citaro', 'Tourismo'],
    'Price': [4580000, 6000000, 7500000, 17100000, 5050000, 7350000, 11500000, 16000000, 6000000, 7500000, 9900000, 24800000, 33000000, 220000000, 8000000, 7500000, 9000000, 6500000, 11000000, 21700000, 9600000, 8500000],
    'Car_Type': ['Sedan', 'Sedan', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'SUV', 'Hatchback', 'Hatchback', 'Hatchback', 'Sports', 'Sports', 'Sports', 'Van', 'Van', 'Van', 'Commercial Truck', 'Commercial Truck', 'Commercial Truck', 'Buses', 'Buses'],
    'Fuel_Type': ['Diesel', 'Petrol','Petrol', 'Hybrid', 'Diesel', 'Diesel', 'Diesel', 'Hybrid', 'Electric', 'Electric', 'Electric', 'Petrol', 'Petrol', 'Petrol', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel']
}

mercedes_data = pd.DataFrame(data)

mercedes_data.index = range(1, len(mercedes_data) + 1)

def main():
    st.title("Mercedes-Benz Vehicle Models Explorer")

    st.subheader("Mercedes-Benz Vehicle Models Data")
    st.write(mercedes_data)

    st.sidebar.header("Filter Vehicle Models")

    # Allow null options for filtering
    price_options = ["Select Price"] + list(mercedes_data['Price'].unique())
    selected_price = st.sidebar.selectbox("Select Price", price_options)

    car_type_options = ["Select Vehicle Type"] + list(mercedes_data['Car_Type'].unique())
    selected_car_type = st.sidebar.selectbox("Select Vehicle Type", car_type_options)

    fuel_type_options = ["Select Fuel Type"] + list(mercedes_data['Fuel_Type'].unique())
    selected_fuel_type = st.sidebar.selectbox("Select Fuel Type", fuel_type_options)

    # Apply filters based on user selection
    if selected_price != "Select Price":
        filtered_data = mercedes_data[mercedes_data['Price'] == selected_price]
    else:
        filtered_data = mercedes_data

    if selected_car_type != "Select Vehicle Type":
        filtered_data = filtered_data[filtered_data['Car_Type'] == selected_car_type]

    if selected_fuel_type != "Select Fuel Type":
        filtered_data = filtered_data[filtered_data['Fuel_Type'] == selected_fuel_type]

    filtered_data.index = range(1, len(filtered_data) + 1)

    st.subheader("Filtered Vehicle Models Data")
    st.write(filtered_data)

if __name__ == "__main__":
    main()
