# Wisconsin City Clustering
This project uses **K-Means** clustering to analyze and visualize the population distribution of Wisconsin. The goal is to cluster population data where each coordinate represents up to **10,000 people**. The program uses K-Means to segment the state into **190 clusters** based on the geographical coordinates of population centers.

The goal of this project is to see how accurate a computer can cluster the population of Wisconsin (2020) to form cities when compared to
where real life cities have formed.

## Dataset
The dataset used for this clustering analysis contains the population coordinates for various locations across Wisconsin. The coordinates are modified to simulate the population distribution across the state.
- Population Coordinates (`wis_pop_coord.csv`): Coordinates representing the population distribution.
- City Coordinates (`cleaned_city_coords.csv`): Coordinates for the centroids of Wisconsin cities, used for visual reference.
The data was initially sourced from [Wisconsin Geospatial Data](https://geodata.wisc.edu/catalog/367B52FB-6AEC-47F9-978D-29D1876AF057/metadata?utm_source=chatgpt.com) and [2020 Cartographic Boundary File](https://catalog.data.gov/dataset/2020-cartographic-boundary-file-shp-current-place-for-wisconsin-1-500000).

## Installation
To run this project, clone this repository and install the required dependencies. You can use the following command to install the necessary libraries:
```
pip install -r requirements.txt
```

### Requirements
- pandas
- matplotlib
- scikit-learn
- numpy

## How to Run
1. Clone this repository or download the necessary files.
2. Ensure that the datasets `wis_pop_coord.csv` and `cleaned_city_coords.csv` are available in the same directory as the Python script.
3. Run the Python script `wisc_cities_clustering.py` to perform the K-Means clustering analysis.

```
python wisc_cities_clustering.py
```

### Clustering the Population
The script will:
- Read the population coordinates and perform K-Means clustering with 190 clusters.
- Visualize the population distribution using a scatter plot.
- Highlight the cluster centers on the scatter plot.
- Overlay actual city locations to compare clustering accuracy.

### Example Output
- A hexbin scatter plot showing the population distribution across Wisconsin.
- A scatter plot of the population data, with the cluster centroids represented as colored points, with the color depending on the population density.
- A final scatter plot comparing the actual city locations (shown in red) with the predicted clusters.

## Results
After running the script, you’ll see:
- A plot showing the population distribution across the state with color-coded cluster centers.
- A comparison of the K-Means clustering results with actual city centroid locations.

## Interpretation
### Population Density Map
![wisc-pop-density-hexbin](https://github.com/user-attachments/assets/bbcf4164-f438-4a4d-b774-3e873099b5e9)
### Computer's Predicted Placement of Cities
![predicted-wisc-cities-map](https://github.com/user-attachments/assets/a7d6d13f-b2ba-49f7-998e-ed3e7e0c47d7)
### Actual City Placements
![actual-wisc-cities-map](https://github.com/user-attachments/assets/e8809366-90d5-471f-8a63-0ed30434674a)

Overall, the predicted placement for the cities was remarkably well. The computer did a great job at placing the more populated cities in almost the exact location of their real-life counterparts. The less populated cities resorted to being placed more uniform across the rest of the population. This is especially noticeable in the northern part of the state, as more cities were predicted to be there than there actually are. This is due to the high amount of towns and villages that are actually up north, which are not a part of the prediction. Most people have higher travel distances to incorperated cities up north, which is something the computer does not know. Instead, the clustering algorithm ended up spreading out cities across the population that lives in towns and villages. The end result was still remarkeably accurate and is impressive to see the computer calculate just based on population density.

