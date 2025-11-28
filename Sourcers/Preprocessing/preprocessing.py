import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


#-----------------------------------------
# Data Loading Class
#-----------------------------------------

class DataLoad:
    def __init__(self, url):
        self.url = url

    def __call__(self):
        response = requests.get(self.url)
        response.raise_for_status() 
        data = response.json()
        df = pd.DataFrame(data)
        return df

#-----------------------------------------
# Data Searching and Filtering Class
#-----------------------------------------

class DataScearch:
    def __init__(self, df):
        self.df = df

    def __call__(self, column, value):
        if column not in self.df.columns:
            
           raise ValueError(f"Column '{column}' does not exist in the DataFrame")

        elif self.df[column].dtype == "O":
            
            result = self.df[self.df[column].str.contains(value)]
            
        else:
        
            result = self.df[self.df[column] == value]
    
        return result
    
    # Method to extract CO2 readings and corresponding timestamps from the filtered DataFrame
    def __co2read__(self, result):

        if result.empty:
    
            raise ValueError("The filtered DataFrame is empty")
        
        co2_array = result["co2readings"].dropna().to_numpy()
        co2_array = np.concatenate(co2_array)
        
        start_time = datetime.fromisoformat(result.iloc[0]["startOfMeasurement"])  
        interval = int(result.iloc[0]["interval"])
        time_array = np.array([start_time + timedelta(minutes=int(i * interval)) for i in range(len(co2_array))])


        return co2_array, time_array


#-----------------------------------------
# Data Cleaning Class
#-----------------------------------------

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def __call__(self, method="mean"):

        # clean empty strings and common NaN representations of pandas and numpy null values
        self.df = self.df.replace(
            [r'^\s*$', 'NaN', 'nan', 'NAN', 'N/A', 'None', None],
            np.nan,
            regex=True
        )

        # Identify columns with list or dict types to exclude them from imputation
        list_cols = [
            col for col in self.df.columns 
            if self.df[col].apply(lambda x: isinstance(x, (list, dict))).any()
        ]

        # numeric columns imputation
        num_cols = self.df.select_dtypes(include='number').columns.difference(list_cols)
        if method == "mean":
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
        elif method == "median":
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].median())
        else:
            raise ValueError('Use mean or median')

        # string/categorical columns imputation
        cat_cols = self.df.select_dtypes(exclude=['number']).columns.difference(list_cols)
        for col in cat_cols:
            mode_series = self.df[col].mode()
            if not mode_series.empty:
                self.df[col].fillna(mode_series.iloc[0], inplace=True)

        return self.df

#-----------------------------------------
# Data Printing Class
#-----------------------------------------

class DataPrint:
    def __init__(self, df):
        self.df = df

    def __call__(self, columns):

        for col in columns:
            if col not in self.df.columns:
                print(f'The column {col} does not exist in the DataFrame.\n')
                continue

            counts = self.df[col].value_counts(dropna=False)
            total = len(self.df[col])
            print(f'\n{counts}')
            print(f'Size: {total}\n')

#-----------------------------------------
# CO2 Classification Class
#-----------------------------------------

class ClassifierCO2:
    def __init__(self):
        pass

    @staticmethod

    def classify_co2(ppm):
        if ppm < 1000:
            return "Safe"
        elif ppm < 2000:
            return "Moderate"
        elif ppm < 5000:
            return "High"
        elif ppm < 10000:
            return "Risky"
        elif ppm < 15000:
            return "Dangerous"
        elif ppm < 30000:
            return "Severe"
        elif ppm < 50000:
            return "Critical"
        else:
            return "Lethal"

#-----------------------------------------
# Ventilation Classification Class
#-----------------------------------------

class VentilationClassifier:
    def __init__(self):
        pass
    
    @staticmethod

    def classify_ventilation(row):
        mech = str(row["ventilationSystem"]).strip().lower() == "true"
        nat = str(row["windowsOpen"]).strip().lower() == "true"
        
        if mech and nat:
            return "both"
        elif mech:
            return "mechanical"
        elif nat:
            return "natural"
        else:
            return "none"

#-----------------------------------------
# Time of Day Classification Class
#-----------------------------------------

class TimeOfDayClassifier:
    
    def __init__(self):
        pass

    @staticmethod
    def classify_hour(dt):

        hour = dt.hour
        if 21 <= hour or hour < 3:
            return "Midnight"
        elif 3 <= hour < 9:
            return "Morning"
        elif 9 <= hour < 15:
            return "Noon"
        elif 15 <= hour < 21:
            return "Afternoon"
        else:
            return np.nan

    def classify_list(self, time_list):

        if not isinstance(time_list, list) or len(time_list) == 0:
            return np.nan
        try:
            t = pd.to_datetime(time_list)
            return self.classify_hour(t[0])
        except Exception:
            return np.nan

#-----------------------------------------
# Time Series Construction Class
#-----------------------------------------

class TimeSeries:
    def __init__(self, df):
        self.df = df

    def __call__(self, readings_col, start_col, interval_col, absolute=True): #True absolute time, False relative time

        def build_times(row):
            readings = row[readings_col]
            interval = row[interval_col]
            if not isinstance(readings, list) or len(readings) == 0:
                return np.nan
            if pd.isna(interval) or interval <= 0:
                return np.nan
            
            dt = interval * 60.0 
            rel_times = np.arange(0, len(readings) * dt, dt)
            
            if absolute:
                start_time = pd.to_datetime(row[start_col])
                abs_times = [start_time + pd.to_timedelta(t, unit='s') for t in rel_times]
                return abs_times
            else:
                return list(rel_times)

        self.df["timelist"] = self.df.apply(build_times, axis=1)
        return self.df

#-----------------------------------------
# Class to convert time to seconds
#-----------------------------------------

class TimeSeconds:
    def __init__(self, time_array):
        self.time_array = time_array
    
    def __call__(self):
        delta = [t - self.time_array[0] for t in self.time_array]
        time_seconds = np.array([d.total_seconds() for d in delta])
        return time_seconds  

