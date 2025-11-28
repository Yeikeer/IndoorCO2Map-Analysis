import pandas as pd
import numpy as np
from scipy.stats import shapiro, ks_2samp, kruskal, chi2_contingency


#-----------------------------------------
# Feature Statistics Extraction Class
#-----------------------------------------

class FeatureExtractor:
    def __init__(self, df, list_col):
        self.df = df
        self.list_col = list_col

    def __call__(self, prefix=None):

        if prefix is None:
            prefix = self.list_col

        self.df[f"{prefix}Med"] = self.df[self.list_col].apply(np.median)
        self.df[f"{prefix}Std"] = self.df[self.list_col].apply(np.std)
        self.df[f"{prefix}Var"] = self.df[self.list_col].apply(np.var)
        self.df[f"{prefix}Min"] = self.df[self.list_col].apply(np.min)
        self.df[f"{prefix}Max"] = self.df[self.list_col].apply(np.max)
        self.df[f"{prefix}Range"] = self.df[self.list_col].apply(lambda x: np.max(x) - np.min(x))
        self.df[f"{prefix}RMS"] = self.df[self.list_col].apply(lambda x: np.sqrt(np.mean(np.square(x))))
        self.df[f"{prefix}CV"] = self.df[f"{prefix}Std"] / self.df[f"{prefix}Med"]

        return self.df

#-----------------------------------------
# Temporal Feature Statistics Extraction Class
#-----------------------------------------

class TemporalFeatureExtractor:

    def __init__(self, df, co2_col, time_col):
        self.df = df
        self.co2_col = co2_col
        self.time_col = time_col

    def convert_s(self, time_list):
        if not isinstance(time_list, list) or len(time_list) < 2:
            return None
        try:
            t = pd.to_datetime(time_list)
            return np.array([(ti - t[0]).total_seconds() for ti in t])
        except Exception:
            return None

    def __call__(self):
        def safe_polyfit(t, y, deg):
            try:
                if t is None or len(t) < 3:
                    return np.nan
                return np.polyfit(t, y, deg)[0]
            except Exception:
                return np.nan

        self.df["co2readingsSlope"] = self.df.apply(
            lambda r: safe_polyfit(self.convert_s(r[self.time_col]), r[self.co2_col], 1),
            axis=1
        )

        self.df["co2readingsCurvature"] = self.df.apply(
            lambda r: safe_polyfit(self.convert_s(r[self.time_col]), r[self.co2_col], 2),
            axis=1
        )

        self.df["co2readingsMean_diff"] = self.df[self.co2_col].apply(
            lambda x: np.mean(np.abs(np.diff(x))) if isinstance(x, list) and len(x) > 1 else np.nan
        )

        self.df["co2readingsStd_diff"] = self.df[self.co2_col].apply(
            lambda x: np.std(np.diff(x)) if isinstance(x, list) and len(x) > 1 else np.nan
        )

        return self.df

#-----------------------------------------
# Class for extracting the derivative and second derivative
#-----------------------------------------

class Derivative:
    def __init__(self, x, t):
        self.x = x
        self.t = t
    
    def __call__(self):
        #diff is the discrete difference for the forward derivative
        dx = np.diff(self.x) 
        dt = np.diff(self.t)
        derivative = dx / dt
        return derivative

class SecondDerivative(Derivative):
    def __call__(self):
        first_derivative = super().__call__()
        dx2 = np.diff(first_derivative)
        dt = np.diff(self.t)[1:]  # Second derivative fit [All except the first]
        second_derivative = dx2 / dt
        return second_derivative

#-----------------------------------------
# Kolmogorov–Smirnov Test
#-----------------------------------------

class KolmogorovSmirnovTest:

    def __init__(self, data):
        self.data = np.array(data)

    def __call__(self):
        data = self.data[~np.isnan(self.data)]
        if len(data) < 3:
            return {"test": "KS", "error": "Insufficient data"}

        mean = np.mean(data)
        std = np.std(data)

        ref = np.random.normal(mean, std, size=len(data))

        stat, p = ks_2samp(data, ref)

        return {"test": "KS", "statistic": stat, "pvalue": p}


#-----------------------------------------
# Shapiro–Wilk Test
#-----------------------------------------

class ShapiroWilkTest:
    def __init__(self, data):
        self.data = np.array(data)

    def __call__(self):
        data = self.data[~np.isnan(self.data)]
        if len(data) < 3:
            return {"test": "Shapiro", "error": "Insufficient data"}

        stat, p = shapiro(data)
        return {"test": "Shapiro", "statistic": stat, "pvalue": p}


#-----------------------------------------
# Kruskal–Wallis
#-----------------------------------------

class KruskalWallisTest:
    def __init__(self, groups: dict):
        self.groups = groups

    def __call__(self):
        data = [
            np.array(values)[~np.isnan(values)]
            for values in self.groups.values()
        ]
        data = [g for g in data if len(g) > 1]
        if len(data) < 2:
            return {"test": "Kruskal-Wallis", "statistic": np.nan, "pvalue": np.nan}
        try:
            stat, p = kruskal(*data)
        except Exception:
            stat, p = np.nan, np.nan
        return {"test": "Kruskal-Wallis", "statistic": stat, "pvalue": p}

#-----------------------------------------
# Chi-Cuadrado
#-----------------------------------------

class ChiSquareTest:

    def __init__(self, contingency):
        self.contingency = contingency

    def __call__(self):
        stat, p, dof, expected = chi2_contingency(self.contingency)
        return {
            "test": "Chi-Square",
            "statistic": stat,
            "pvalue": p,
            "dof": dof,
            "expected": expected
        }