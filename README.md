

### Santiago Correa Restrepo
### santiagocorrea251469@correo.itm.edu.co

---

<br/>

# Indoor CO₂ Map Analysis

## Context 

Human beings spend a large proportion of their time — often 80 %–90 % — in indoor spaces such as homes, offices, classrooms, and public buildings. Carbon dioxide (CO₂), exhaled by occupants, serves as a widely accepted proxy for assessing ventilation and indoor air quality. Elevated indoor CO₂ levels often indicate insufficient ventilation, which can lead to the accumulation of exhaled air and aerosolized contaminants — increasing risks of poor air quality, discomfort, diminished cognitive performance, and even transmission of airborne pathogens in crowded or poorly ventilated spaces.

Monitoring CO₂ indoors is thus critical not only for comfort and health, but also for providing objective indicators to guide ventilation improvements or behavior changes.


## About the IndoorCO2Map Project

The IndoorCO2Map project is an open‑source, crowd‑sourced initiative to collect and share CO₂ measurements from diverse non‑residential buildings — shops, schools, hospitals, restaurants, offices, and more. The idea is to build a global dataset that reflects real indoor air conditions across different types of buildings and geographies. 

By contributing with sensor data, anyone can help map how indoor air quality varies across spaces and evaluate ventilation adequacy in a data‑driven manner. As more data accumulate, the dataset can become a powerful resource for scientific analysis, policy recommendations, and public health advocacy.

This repository — **IndoorCO2Map-Analysis** — builds upon that vision: it collects, processes, analyzes, visualizes, and assesses CO₂ datasets (raw and processed) to investigate indoor air quality, ventilation classes, temporal patterns, and co‑variates in a systematic way.  

## Repository Structure

```
IndoorCO2Map-Analysis/
|
├── Data/
│   ├── Processed/
│   │   └── indoorco2map_processed.csv
│   └── Raw/
│       └── indoorco2mapData.json
├── Notebooks/
│   ├── Lab 1/
│   │   ├── Lab 1 .docx
│   │   └── Lab1.ipynb
│   ├── Lab 2/
│   │   ├── Lab 2.docx
│   │   └── Lab2.ipynb
│   ├── Lab 3/
│   │   └── Lab 3.docx
│   └── ML/
│       └── indoorco2map_class.ipynb
├── README.md
├── Results/
│   ├── Figures/
│   │   ├── avg_countries.png
│   │   ├── avg_timeofday.png
│   │   ├── avg_ventilation.png
│   │   ├── count_country.png
│   │   ├── heatmap_metrics.png
│   │   ├── mapa_co2_count.html
│   │   ├── mapa_co2_prom.html
│   │   ├── pairplot_features.png
│   │   ├── ppmv_co2.jpg
│   │   ├── significant_features.png
│   │   └── violin_co2class.png
│   ├── README.md
│   ├── References.bib
│   └── Tables/
│       ├── chi_square_tests.png
│       ├── kolmogorov_tests.png
│       └── kruskal_tests.png
├── Sourcers/
│   ├── Analysis/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── analysis.cpython-310.pyc
│   │   └── analysis.py
│   ├── Preprocessing/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── preprocessing.cpython-310.pyc
│   │   └── preprocessing.py
│   ├── Visualization/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── visualization.cpython-310.pyc
│   │   └── visualization.py
│   ├── __init__.py
│   └── __pycache__/
│       └── __init__.cpython-310.pyc
├── Test/
│   ├── complexity_analysis.ipynb
│   └── exlample_test.ipynb
├── main.py
├── mapa.py
├── repo_structure.md
└── requeriments.txt
```

### Component Details

- **`Data/Raw/`**: contains the original input files with unprocessed CO₂ data—raw measurements, times, metadata, etc.  
- **`Data/Processed/`**: contains the transformed data after cleaning, feature extraction, and classification, ready for analysis.
- **`Results/Figures/`**: generated after running `main.py`. Includes graphs such as CO₂ distribution by country, ventilation, time-of-day, distribution by class, correlation matrices, pairplots, etc.  
- **`Results/Tables/`**: contains statistical test results (e.g., normality tests, nonparametric tests, contingency tables), as well as the final export of processed data in CSV.
- **`main.py`**: the heart of the project—orchestrates the entire data flow: loading, cleaning, extraction, classification, visualization, and export. It allows the entire analysis pipeline to be reproduced with a single command.
- **`requirements.txt`**: list of Python dependencies (pandas, matplotlib/seaborn, statistical tests, etc.) for reproducibility.


## How to Run the Project 🚀

1. Clone the repository:  
   ```bash
   git clone https://github.com/Yeikeer/IndoorCO2Map-Analysis.git
   cd IndoorCO2Map-Analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the full pipeline:

   ```bash
   python main.py
   ```

4. Results: once `main.py` finishes, you will find:

   * Graphs in `Results/Figures/` (heat maps, bar charts, violin plots, pair plots, etc.)
   * Statistical tables in `Results/Tables/`
   * Processed data in `Data/Processed/indoorco2map_processed.csv`


## Why This Matters

By systematizing the collection, cleaning, analysis, and visualization of indoor CO₂ data, this project provides a **reproducible and flexible tool** for assessing indoor air quality. It offers a framework for:

* Analyzing ventilation and CO₂ patterns in real buildings.
* Perform statistical tests on distribution, CO₂ classes, variability by country, time of day, type of ventilation, etc.
* Visualize results in a clear and standardized way.
* Build a public dataset that can serve as a basis for future research, ventilation policies, environmental health, or architectural design recommendations.
