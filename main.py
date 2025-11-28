import time
import psutil
import os
import pandas as pd

# Import modules
from Sourcers.Preprocessing import *
from Sourcers.Analysis import *
from Sourcers.Visualization import *



# -----------------------------------------
# Helpers for memory and time tracking
# -----------------------------------------

def get_memory_mb():
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)


# -----------------------------------------
# main function
# -----------------------------------------

def main():

    print("\n--------------- Indoor CO2 Map Analysis Start ---------------\n")

    t0 = time.time()
    mem0 = get_memory_mb()

    # Paths
    IMAGES_PATH = os.path.join("Results", "Figures")
    TABLES_PATH = os.path.join("Results", "Tables")
    PROCESSED_DATA_PATH = os.path.join("Data", "Processed")
    URL = "https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/refs/heads/main/Data/Raw/indoorco2mapData.json"

    # Load Data-------
    df = DataLoad(URL)()
    
    # Cleaning-------
    df = DataCleaner(df)()

    # Time Series------- 
    ts = TimeSeries(df)
    df = ts("co2readings", "startOfMeasurement", "interval", absolute=True)

    # Features--------
    df = FeatureExtractor(df, list_col="co2readings")()
    df = TemporalFeatureExtractor(df, co2_col="co2readings", time_col="timelist")()

    # Classification--------
    # -CO2 Level Classification 
    df["co2class"] = df["co2readingsMed"].apply(ClassifierCO2.classify_co2)
    counts = df["co2class"].value_counts()
    valid_classes = counts[counts >= 10].index.tolist()
    df = df[df["co2class"].isin(valid_classes)].copy()
    # -Ventilation Classification 
    df["ventilationclass"] = df.apply(VentilationClassifier.classify_ventilation, axis=1)
    # -Time of Day Classification
    tod = TimeOfDayClassifier()
    df["timeday"] = df["timelist"].apply(tod.classify_list)

    # Visualization-------

    #-count by country
    country_counts = df["countryName"].value_counts().reset_index()
    country_counts.columns = ["countryName", "count"]
    country_counts10 = country_counts[country_counts["count"] >= 10].reset_index(drop=True)

    # Bar plot of counts by country
    pb = PlotBuilder(country_counts10)
    fig = pb.bar(
        x="countryName",
        y="count",
        title="Count by country",
        horizontal=True
    )
    FigureExporter(fig).save(os.path.join(IMAGES_PATH, "count_country.png"))

    #-Top countries by median CO2 levels
    filtered_df = df[df["countryName"].isin(country_counts10["countryName"])].copy()

    co2_avg_country = (
        filtered_df.groupby("countryName")["co2readingsAvg"]
        .mean()
        .reset_index()
        .rename(columns={"countryName": "Country", "co2readingsAvg": "Avg_CO2"})
    )

    co2_avg_country = (
        co2_avg_country.sort_values(by="Avg_CO2", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )

    # Bar plot of top 10 countries by median CO2 levels
    pb2 = PlotBuilder(co2_avg_country)
    fig2 = pb2.bar(
        x="Country",
        y="Avg_CO2",
        title="Top 10 Countries by Median CO2 Levels",
        horizontal=True
    )
    FigureExporter(fig2).save(os.path.join(IMAGES_PATH, "avg_countries.png"))

    #-CO2 Prom kind of ventilation
    vent_means = (
        df.groupby("ventilationclass")["co2readingsAvg"]
        .mean()
        .reset_index()
        .rename(columns={"ventilationclass": "Ventilation",
                        "co2readingsAvg": "Avg_CO2"})
        .sort_values(by="Avg_CO2", ascending=False)
        .reset_index(drop=True)
    )

    # Bar plot of counts by ventilation class
    pb3 = PlotBuilder(vent_means)
    fig3 = pb3.bar(
        x="Ventilation",
        y="Avg_CO2",
        title="Average CO2 Levels by Ventilation Class",
        horizontal=False
    )
    FigureExporter(fig3).save(os.path.join(IMAGES_PATH, "avg_ventilation.png"))

    #-CO2 Prom by time of day
    timeday_means = (
        df.groupby("timeday")["co2readingsAvg"]
        .mean()
        .reset_index()
        .rename(columns={"timeday": "TimeOfDay",
                        "co2readingsAvg": "Avg_CO2"})
        .sort_values(by="Avg_CO2", ascending=False)
        .reset_index(drop=True)
    )

    # Bar plot of counts by time of day
    pb4 = PlotBuilder(timeday_means)
    fig4 = pb4.bar(
        x="TimeOfDay",
        y="Avg_CO2",
        title="Average CO2 Levels by Time of Day",
        horizontal=False
    )
    FigureExporter(fig4).save(os.path.join(IMAGES_PATH, "avg_timeofday.png"))

    #-CO2 levels by CO2 class
    #Violin plot of CO2 levels by CO2 class
    pb4 = PlotBuilder(df)

    fig4 = pb4.violin(
        column="co2readingsAvg",   # variable numérica
        by="co2class",             # variable categórica
        title="CO2 Distribution by CO2 Class"
    )

    FigureExporter(fig4).save(os.path.join(IMAGES_PATH, "violin_co2class.png"))

    #-Correlation matrix
    corr = df[
        ["co2readingsAvg", "co2readingsMed", "co2readingsStd", "co2readingsVar",
        "co2readingsRange", "co2readingsRMS", "co2readingsCV",
        "co2readingsSlope", "co2readingsCurvature",
        "co2readingsMean_diff", "co2readingsStd_diff"]
    ].corr()

    # Heatmap of correlation matrix
    pb5 = PlotBuilder(corr)
    fig5 = pb5.heatmap(
        title="Correlation Heatmap of CO2 Metrics",
        annot=True
    )

    FigureExporter(fig5).save(os.path.join(IMAGES_PATH, "heatmap_metrics.png"))

    #-Feuture comparatives plots
    cols = df[[
        "co2class",               # Classifier
        "co2readingsMed",          # CO2 median
        "co2readingsStd",          # Standard deviation
        "co2readingsCV",           # Coefficient of Variation
        "co2readingsSlope",        # Slope
        "co2readingsCurvature",    # Curvature
        "co2readingsStd_diff",     # Variability of changes
    ]]

    # Pairplot of selected features by CO2 class
    pb6 = PlotBuilder(cols)
    fig6 = pb6.pairplot(
        hue="co2class",
        diag_kind="kde",
        title="Pairplot of CO2 Features by CO2 Class"
    )

    FigureExporter(fig6).save(os.path.join(IMAGES_PATH, "pairplot_features.png"))

    # Stadistics tests -------
    # Numeric variables of interest
    numeric_features = [
        "co2readingsMed",
        "co2readingsStd",
        "co2readingsCV",
        "co2readingsSlope",
        "co2readingsCurvature",
        "co2readingsStd_diff"
    ]

    # Categorical variables of interest
    categorical_features = [
        "timeday",
        "ventilationclass",
        "countryName",
        "osmKey",
        "co2class"   # Classifier
    ]

    #-Kolmogorov-Smirnov Test for normality
    ks_results = []
    for feature in numeric_features:
        data = df[feature].values
        test = KolmogorovSmirnovTest(data)()
        test["feature"] = feature
        ks_results.append(test)
    ks_df = pd.DataFrame(ks_results)[["feature", "test", "statistic", "pvalue"]]
    TableExporter(ks_df).to_png(os.path.join(TABLES_PATH, "kolmogorov_tests.png"))

    #-Kruskal-Wallis Test for differences between groups
    kw_results = []
    for feature in numeric_features:
        groups = df.groupby("co2class")[feature].apply(list).to_dict()
        test = KruskalWallisTest(groups)()
        test["feature"] = feature
        kw_results.append(test)
    kw_df = pd.DataFrame(kw_results)[["feature", "test", "statistic", "pvalue"]]
    TableExporter(kw_df).to_png(os.path.join(TABLES_PATH, "kruskal_tests.png"))

    #-Chi-Squared Test for independence between categorical variables
    chi_results = []
    for cat in categorical_features:
        contingency = pd.crosstab(df[cat], df["co2class"])
        test = ChiSquareTest(contingency)()
        chi_results.append({
            "variable": cat,
            "statistic": test["statistic"],
            "pvalue": test["pvalue"],
            "dof": test["dof"]
        })
    chi_df = pd.DataFrame(chi_results)
    TableExporter(chi_df).to_png(os.path.join(TABLES_PATH, "chi_square_tests.png"))

    # Visualization final -------

    #-Multi box plot
    significant_features = kw_df[kw_df["pvalue"] < 0.05]["feature"].tolist()
    pb7 = PlotBuilder(df)
    fig7 = pb7.multi_boxplot(
        columns=significant_features,
        by="co2class",
        title="Significant Features by CO2 Class"
    )

    FigureExporter(fig7).save(os.path.join(IMAGES_PATH, "significant_features.png"))

    # Export processed data -------
    TableExporter(df).to_csv(PROCESSED_DATA_PATH, "indoorco2map_processed.csv")

    # Performance ------

    t1 = time.time()
    mem1 = get_memory_mb()

    print("\n--------------- Indoor CO2 Map End ---------------\n")

    print("\n--- Performance ---")
    print(f"Total Time: {t1 - t0:.2f} s")
    print(f"Used Memory: {mem1 - mem0:.2f} MB")

# -----------------------------------------
# Entry point
# -----------------------------------------

if __name__ == "__main__":
    main()
