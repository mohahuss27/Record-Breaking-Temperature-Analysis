# Record-Breaking Temperature Analysis

## Overview
This project demonstrates **data analysis and visualization skills** by examining historical temperature trends in **Ann Arbor, Michigan**. Using daily climate data from **2005–2014**, the analysis identifies **record-breaking temperatures in 2015**, providing actionable insights into extreme weather events and climate variability.

> Demonstrates hands-on experience in Python, data manipulation, statistical analysis, and time series visualization.

## Highlights / Key Contributions
* **Data Cleaning & Preprocessing** – Handled missing data, converted units, and prepared time-series datasets for analysis  
* **Statistical Analysis** – Calculated daily max/min temperatures and historical baselines to detect anomalies  
* **Data Visualization** – Created clear and insightful plots that highlight record-breaking temperature events  
* **Climate Insights** – Identified trends in extreme weather and daily temperature fluctuations  

## Technologies & Tools
* **Python 3.x** – Core programming language  
* **Pandas** – Efficient data handling and processing  
* **Matplotlib** – Visualization and plotting  
* **Jupyter Notebook** – Interactive development and demonstration  

## Dataset
Data sourced from the [GHCN-Daily dataset](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) (Global Historical Climatology Network daily) by **NCEI**, containing daily climate records from thousands of global land-based stations.

### Key Data Fields
* **id** – Station identification code  
* **date** – Date in `YYYY-MM-DD` format  
* **element** – Type of measurement (`TMAX` = max temp, `TMIN` = min temp)  
* **value** – Measurement value (tenths of °C)  

## Skills Demonstrated
* Data cleaning and preprocessing  
* Time series analysis and exploratory data analysis (EDA)  
* Statistical computation and anomaly detection  
* Data visualization best practices  
* Python programming and Jupyter Notebook workflow  

## Setup & Requirements
* **Python 3.x**  
* **pandas**  
* **matplotlib**  

Install dependencies:
```bash
pip install pandas matplotlib
```

## Usage
1. Ensure the data file `fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv` is in the same directory.
2. Open `weather_analysis.ipynb` in Jupyter Notebook or JupyterLab.
3. Run the cells in order to load data, preprocess, analyze, and visualize the results.

The notebook will generate a plot showing temperature records from 2005-2014 and highlight 2015 record-breaking temperatures.

## License
This project is open-source. Feel free to use and modify.
