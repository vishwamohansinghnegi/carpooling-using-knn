import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Function to calculate Euclidean distance
def euclidean(lat1, lon1, lat2, lon2):
    return np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# Loading data
@st.cache_data
def load_data():
    data = pd.read_csv('uber.csv')
    data.drop(columns=['pickup_datetime'], axis=1 , inplace=True)
    data.dropna(inplace=True)
    return data

df = load_data()

# Initializing session state
if "pickup_coords" not in st.session_state:
    st.session_state.pickup_coords = None

if "dropoff_coords" not in st.session_state:
    st.session_state.dropoff_coords = None

if "carpool_results" not in st.session_state:
    st.session_state.carpool_results = None

# Title
st.title("Carpooling System with KNN")

# Pickup Map
st.write("### Select Pickup Location:")
pickup_map = folium.Map(location=[40.730610, -73.935242], zoom_start=12)

if st.session_state.pickup_coords:
    folium.Marker(
        location=[st.session_state.pickup_coords["lat"], st.session_state.pickup_coords["lng"]],
        popup="Pickup Location",
        icon=folium.Icon(color="red"),
    ).add_to(pickup_map)

pickup_output = st_folium(pickup_map, width=700, height=500)

if pickup_output.get("last_clicked"):
    st.session_state.pickup_coords = pickup_output["last_clicked"]

if st.session_state.pickup_coords:
    st.write(f"**Selected Pickup Coordinates:** {st.session_state.pickup_coords}")

# Dropoff Map
st.write("### Select Dropoff Location:")
dropoff_map = folium.Map(location=[40.741895, -73.989308], zoom_start=12)

if st.session_state.dropoff_coords:
    folium.Marker(
        location=[st.session_state.dropoff_coords["lat"], st.session_state.dropoff_coords["lng"]],
        popup="Dropoff Location",
        icon=folium.Icon(color="blue"),
    ).add_to(dropoff_map)

dropoff_output = st_folium(dropoff_map, width=700, height=500)

if dropoff_output.get("last_clicked"):
    st.session_state.dropoff_coords = dropoff_output["last_clicked"]
    st.experimental_rerun()

if st.session_state.dropoff_coords:
    st.write(f"**Selected Dropoff Coordinates:** {st.session_state.dropoff_coords}")

# Find Carpool Options Button
if st.button("Find Carpool Options"):
    if st.session_state.pickup_coords and st.session_state.dropoff_coords:
        user_pickup = np.array([st.session_state.pickup_coords["lat"], st.session_state.pickup_coords["lng"]])
        user_dropoff = np.array([st.session_state.dropoff_coords["lat"], st.session_state.dropoff_coords["lng"]])
        
        # Calculate Euclidean distances
        pickup_distances = []
        dropoff_distances = []
        
        for index, row in df.iterrows():
            pickup_distances.append(
                euclidean(row["pickup_latitude"], row["pickup_longitude"], user_pickup[0], user_pickup[1])
            )
            dropoff_distances.append(
                euclidean(row["dropoff_latitude"], row["dropoff_longitude"], user_dropoff[0], user_dropoff[1])
            )
        
        df["pickup_distance"] = pickup_distances
        df["dropoff_distance"] = dropoff_distances
        df["total_distance"] = df["pickup_distance"] + df["dropoff_distance"]

        # Use KNN for finding the nearest neighbors
        knn = NearestNeighbors(n_neighbors=3, metric="euclidean")
        distances = df[["pickup_distance", "dropoff_distance"]].values
        knn.fit(distances)
        _, indices = knn.kneighbors([[0, 0]])  # User distances set to 0
        
        st.session_state.carpool_results = df.iloc[indices[0]]

        st.success("Carpool options found!")
    else:
        st.error("Please select both pickup and dropoff locations.")

# Display Carpool Results
if st.session_state.carpool_results is not None:
    st.write("### Carpool Options:")
    st.dataframe(st.session_state.carpool_results)

    # Visualize Results on a Map
    result_map = folium.Map(location=[st.session_state.pickup_coords["lat"], st.session_state.pickup_coords["lng"]], zoom_start=12)

    # Add user markers
    folium.Marker(
        location=[st.session_state.pickup_coords["lat"], st.session_state.pickup_coords["lng"]],
        popup="Your Pickup Location",
        icon=folium.Icon(color="red"),
    ).add_to(result_map)

    folium.Marker(
        location=[st.session_state.dropoff_coords["lat"], st.session_state.dropoff_coords["lng"]],
        popup="Your Dropoff Location",
        icon=folium.Icon(color="blue"),
    ).add_to(result_map)

    # Add carpool options
    for _, row in st.session_state.carpool_results.iterrows():
        folium.Marker(
            location=[row["pickup_latitude"], row["pickup_longitude"]],
            popup="Carpool Pickup Option",
            icon=folium.Icon(color="green"),
        ).add_to(result_map)
        folium.Marker(
            location=[row["dropoff_latitude"], row["dropoff_longitude"]],
            popup="Carpool Dropoff Option",
            icon=folium.Icon(color="orange"),
        ).add_to(result_map)

    st.write("### Nearest Carpool Rides:")
    st_folium(result_map, width=700, height=500)
