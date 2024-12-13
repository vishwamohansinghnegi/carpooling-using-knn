# Carpooling System Using KNN

This project implements a **Carpooling System** that leverages the **K-Nearest Neighbors (KNN)** algorithm to suggest optimal carpooling options based on user-selected pickup and dropoff locations. The system provides an interactive interface using **Streamlit** and **Folium** for data visualization.

---

## Features
- **Interactive Map Interface**:
  - Users can select pickup and dropoff locations on interactive maps.
  - Markers display the selected locations.

- **Carpool Suggestions**:
  - Utilizes the KNN algorithm to find the closest carpool options based on user-provided coordinates.
  - Displays results in a table and visualizes them on a map.

- **Data Preprocessing**:
  - Handles missing data and optimizes the dataset for distance calculations.

- **Visualization**:
  - Pickup and dropoff locations for the user and carpool options are marked on an interactive map using **Folium**.

- **Fare Prediction (EDA)**:
  - Includes an exploratory data analysis (EDA) Jupyter Notebook for analyzing ride data and predicting fares.

---

## Technologies Used
- **Python**
- **Streamlit**: For building an interactive web application.
- **Folium**: For map-based visualizations.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical operations.
- **scikit-learn**: For implementing the KNN algorithm.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vishwamohansinghnegi/carpooling-using-knn.git
   cd carpooling-using-knn
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## How It Works
1. **Dataset**:
   - The project uses a dataset of historical ride data (`uber.csv`) containing pickup and dropoff locations.
   - Preprocessing removes missing values and unnecessary columns (e.g., `pickup_datetime`).

2. **Select Locations**:
   - Users interactively select pickup and dropoff locations on maps.

3. **KNN-Based Matching**:
   - The system calculates Euclidean distances between the user’s selected locations and the dataset locations.
   - Finds the three nearest carpool options based on total distance.

4. **Results**:
   - Displays carpool options in a table with details like pickup and dropoff coordinates.
   - Visualizes the results on a map with markers for user and carpool locations.

5. **EDA and Fare Prediction**:
   - The Jupyter Notebook (`eda_fare_prediction.ipynb`) performs exploratory data analysis and builds a fare prediction model.
   - Due to file size constraints, the trained model (pickle file) is not uploaded but can be retrained using the provided notebook.

---

## Project Structure
- **`app.py`**: Main script to run the Streamlit application.
- **`requirements.txt`**: List of required Python packages.
- **`uber.csv`**: Sample dataset with historical ride data.
- **`eda_fare_prediction.ipynb`**: Jupyter Notebook for EDA and fare prediction.

---

## Usage
1. Launch the app using Streamlit.
2. Use the maps to select a **Pickup** and a **Dropoff** location.
3. Click **Find Carpool Options** to get the nearest carpool rides.
4. View the suggestions in the table and on the map.

---

## Example
1. **Selecting Pickup and Dropoff Locations**:
   - Select locations interactively using maps.
   - View the coordinates displayed below the maps.

2. **Viewing Results**:
   - A table displays the closest carpool options based on the total distance.
   - Markers on the map indicate user and carpool locations for easy visualization.

3. **Fare Prediction**:
   - Analyze ride data trends and predict fares using the notebook.

---

## Contact
Created by Vishwamohan Singh Negi  
For questions or suggestions, feel free to reach out:
- [GitHub Profile](https://github.com/vishwamohansinghnegi)
- [Email](vishwamohansinghnegi@gmail.com)
- [LinkedIn](www.linkedin.com/in/vishwamohan-singh-negi-001b8a257)