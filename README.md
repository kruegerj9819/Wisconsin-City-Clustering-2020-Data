# Wisconsin City Clustering
This project contains two datasets, wisc_pop_coord.csv and cleaned_city_coords.csv. 
The goal of this project is to see how accurate a computer can cluster the population of Wisconsin (2020) to form cities when compared to
where actual cities have formed.

#### wisc_pop_coord.csv
This file contains simulated coordinates of every 100 people in a single block of wisconsin. A block is the smallest form of population data optainable in a dataset. 
The block data used for the simulation is from an archived dataset from UW-Madison found [here](https://geodata.wisc.edu/catalog/367B52FB-6AEC-47F9-978D-29D1876AF057/metadata?utm_source=chatgpt.com).
Using the geographical boundaries of the block data, points are randomly generated inside each block to simulate the population.

#### cleaned_city_coords.csv
This file contains the centroids of each incorporated city geographical boundary in Wisconsin (2020). 
The original data for the city boundaries is from the U.S. Census Bereau found [here](https://catalog.data.gov/dataset/2020-cartographic-boundary-file-shp-current-place-for-wisconsin-1-500000).

## Run Instructions

### Install
- PyCharm Community Edition

### To Run
Navigate to wisc_cities_clustering.py and run the file. You should see the population scatterplot pop up. Once you close the plot, 
the program will continue and will create two more scatterplots (they may be on top of each other).
