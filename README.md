
# Is Your Business Doomed?


A project that performs analysis on Yelp ratings to compare business categories across several metropolitan areas. 
* Business success/failure
* Area competition 
* Potential for future businesses based on category and area.

Results located in notebooks/final

This readme details the steps needed to run all of the notebooks.

## Environments


Both environments in this project are detailed in the folder "anaconda environments"



### 1) /notebooks/prep, /notebooks/analysis, /notebooks/final/RQ1, /notebooks/final/RQ2


All of these notebooks use the environment described in __spec-all.txt__



### 2) notebooks/final/RQ3


This notebook uses Basemap which must must be run using Python 2. 

The enviroment in described in __spec-basemap.txt__

This notebook will produce an error if run in Python 3.



## How to run notebooks


### Step 1: /notebooks/prep
Notebooks are labeled in the order to be run; 100, 200, 300, 400



### Step 2: /notebooks/analysis
Notebooks are labeled in the order to be run; 100, 200, 201, 300, 301, 400, 401



### Step 3: /notebooks/final

Order to be run; RQ1 Final, RQ2 Final



### Step 4: /notebooks/final/RQ3 Final

Change Environment to __spec-basemap__

Run notebook. The first cell can be changed to personalise the map.



## Application used


* [Basemap](https://matplotlib.org/basemap/) - Map making software



### In case of error:
* The map uses a background called 'ESRI_Streetview' that sometimes can fail if the website hosting it goes down.  This will produce '500 Server Error' when the notebook is run. An alternative background is provided in the comments in the makeMap() function.
