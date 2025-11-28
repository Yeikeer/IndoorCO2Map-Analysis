# Global and Local Issues Related to Carbon Dioxide ($\text{CO}_2$)

## 1. Why $\text{CO}_2$ is toxic
Carbon dioxide ($\text{CO}_2$) is a gas that, although a natural component, becomes hazardous in high concentrations. It is colorless, odorless, and tasteless, which makes it particularly dangerous because it is difficult to detect with the human senses. Its accumulation is the basis of the problem addressed by this type of research, because at very high levels it can displace oxygen, leading to toxicity. _(Akhter et al., 2021)_

## 2. Health problems
The main concern with $\text{CO}_2$ arises when its levels exceed **1000 ppm** (parts per million) in enclosed spaces, a threshold that negatively affects **human health and cognitive performance**. The effects of these concentrations range from discomfort and headaches to fatigue. If levels exceed **5000 ppm**, it enters the category of acute toxicity hazard, potentially inducing **hypercapnia** (excess $CO_2$ in the blood). _(WHO Europe, 2010)_

| **$CO_2$ (ppm)**                | **$CO_2$ (%)** | **Effects and Risks**                                                                                 |
| ----------------------------: | ----------: | ----------------------------------------------------------------------------------------------------- |
| **400 – 1,000**              | 0.04 – 0.1  | Typical level in outdoor air (400 ppm) and well-ventilated offices (up to 1,000 ppm). No adverse effects. |
| **1,000 – 2,000**            | 0.1 – 0.2   | May cause mild drowsiness and stuffy air. Indicates insufficient ventilation.                         |
| **2,000 – 5,000**            | 0.2 – 0.5   | Headaches, drowsiness, lack of concentration, and feeling of congestion.                              |
| **5,000**  | 0.5         | Occupational exposure limit for 8 hours/day (PEL, TLV). Prolonged exposure not recommended.            |
| **5,000 – 10,000**           | 0.5 – 1     | Significant increase in symptoms: fatigue, dizziness, mild confusion.                                 |
| **10,000 – 15,000**          | 1 – 1.5     | Nausea, increased heart rate, dizziness, reduced concentration.                                       |
| **15,000 – 30,000**          | 1.5 – 3     | Severe dizziness, strong headaches, risk of prolonged loss of consciousness.                          |
| **30,000 – 50,000**          | 3 – 5       | Acute hypercapnia: confusion, breathing difficulty, loss of consciousness within minutes.              |
| **>50,000**                  | >5          | Severe danger: asphyxiation, convulsions, respiratory arrest, and death within minutes.               |

**Reference:** Table 1: OSHA (Occupational Safety and Health Administration)/NIOSH (National Institute for Occupational Safety and Health)  limit ppm of $CO_2$ indoors

## 3. The global problem of $\text{CO}_2$
The global $\text{CO}_2$ crisis centers on the exponential growth of its atmospheric concentration, with a recorded increase of more than **150%** since 1958. This massive accumulation intensifies the **greenhouse effect** and contributes to **ocean acidification**. The main source of this global problem is **anthropogenic**, driven by the **combustion of fossil fuels** (oil, coal, and gas), which justifies the development of projects that seek to mitigate its effects.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/ppmv_co2.jpg" alt="Figure 1" width="600"/>
</p>

<p align="center">
  <b>Figure 1.</b> Study of the increase in ppm CO₂ globally.  
  Reference: Figure 1 taken from <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121">(NASA., 2025)</a>.
</p>

## 4. Problems it causes indoors
CO₂ becomes a significant risk in indoor spaces, as it tends to accumulate rapidly in poorly ventilated environments. In environments such as classrooms, offices, laboratories, and homes, the concentration of this gas serves as a key indicator of indoor air quality and the possible presence of other harmful pollutants, posing a danger to the respiratory health and well-being of occupants._(Petersen et al., 2016)_

## 5. indoorco2map
Most monitoring efforts focus on atmospheric $\text{CO}_2$, leaving gaps in information about actual indoor exposure. That is why **citizen science** projects such as [indoorco2map.com](https://indoorco2map.com/?lat=48.37962&lng=12.63897&zoom=3.36) are crucial, as they map gas concentrations in public gathering places. The importance of this type of study lies in the fact that it encourages the development of **accessible, accurate, and sustainable** monitoring technologies for risk mitigation._(WHN, 2024)_

<iframe src="https://indoorco2map.com/?lat=19.34553&lng=4.50000&zoom=1.37" 
        loading="lazy" 
        style="width: 100%; height: 650px; border: 1px solid #ccc;" 
        allowfullscreen>
</iframe>

**Reference:** Indoor $CO_2$ Map Project. (n.d.). Retrieved on September 29 - 2025,  https://indoorco2map.com/

## 6. Database analysis

### Count of Participating Countries
The database reveals the geographic distribution of $\text{CO}_2$ measurements through a count of participation by country. This analysis is crucial for evaluating the representativeness of the sample and determining which regions are actively contributing to indoor $\text{CO}_2$ mapping. Generally, a few leading countries account for the majority of entries, which guides the interpretation of the data and suggests areas for promoting citizen science.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/count_country.png" alt="Figure 2" width="600"/>
</p>

### Top 10 Countries with Highest Average CO₂ Emissions
By analyzing the average concentrations of $\text{CO}_2$ per country, the 10 participating nations with the highest levels in their indoor measurements are identified. This segment not only reflects gas pollution levels in enclosed spaces, but can also be an indicator of construction patterns, population density, and poor ventilation habits in these areas, highlighting regions with the highest potential risk to health and cognitive performance.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/avg_countries.png" alt="Figure 3" width="600"/>
</p>

### Concentración de $\text{CO}_2$ por Hora del Día
The graph showing the concentration of $\text{CO}_2$ over a 24-hour period reveals a cyclical pattern directly linked to human activity. CO₂ levels are expected to be lower during the early morning hours and reach significant peaks during peak occupancy hours (morning and afternoon), coinciding with the work and school day. This visualization is essential for understanding when indoor air quality is most critical.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/avg_timeofday.png" alt="Figure 4" width="600"/>
</p>

### Effect of Ventilation on $\text{CO}_2$ Levels
The impact of ventilation on indoor air quality is clearly summarized in the relationship between the condition of windows/doors and the concentration of $\text{CO}_2$ . This analysis shows that, in spaces with closed ventilation, $\text{CO}_2$ levels rise rapidly and exceed comfort thresholds (1000 ppm). In contrast, environments with adequate ventilation maintain concentrations within much safer and more stable ranges, confirming ventilation as the most effective tool against gas accumulation.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/avg_ventilation.png" alt="Figure 5" width="600"/>
</p>

### Distribution of $\text{CO}_2$ by Category
This violin or box plot shows the distribution of $\text{CO}_2$ measurements grouped by different categories (classes). The visualization allows you to compare the **dispersion and central tendency** of gas concentrations between different groups, such as the type of indoor environment (office, classroom, home). The width of each “violin” or the length of the boxes indicates the density and range of $\text{CO}_2$ measurements for each class.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/violin_co2class.png" alt="Figure 6" width="600"/>
</p>

### Feature selection

#### Kolmogorov-Smirnov Normality Test
The **Kolmogorov-Smirnov** test was used to assess whether the distributions of $\text{CO}_2$ in the database conform to a **normal distribution**. This step is crucial in statistical analysis, as normality is a key requirement for the use of parametric tests. The test results, specifically the **p-value**, determine whether the null hypothesis of normality should be rejected, guiding the choice toward nonparametric tests for further analysis.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Tables/kolmogorov_tests.png" alt="Table 2" width="600"/>
</p>

#### Kruskal-Wallis Test (Numeric Variables)
The nonparametric **Kruskal-Wallis** test was used to determine whether there are **significant differences** in the medians of $\text{CO}_2$ concentrations between three or more groups of independent **numerical** variables (for example, comparing the average $\text{CO}_2$ concentration between different types of sensors or between countries). This test is robust and is used when the normality condition is not met, confirming whether the observed variations are statistically relevant.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Tables/kruskal_tests.png" alt="Table 3" width="600"/>
</p>

The hypothesis test gives us all p-values lower than 0.05, therefore explaining that there is a significant difference in all characteristics with respect to the class; However, there are discrepancies with respect to the graphical method, since visually the characteristics co2readingsCV, co2readingsSlope, and co2readingsCurvature do not show this difference compared to the rest (Box Plot). 

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Figures/significant_features.png" alt="Figure 7" width="600"/>
</p>

#### Chi-Square Test ($\chi^2$) (Categorical Variables)
The **Chi-Square test ($\chi^2$)** was applied to examine the existence of a **significant association or relationship** between **categorical** variables within the dataset. For example, it is used to assess whether the ventilation category (open/closed) is related to the $\text{CO}_2$ level category (safe/unsafe). A low *p* value in this test indicates that the dependence between the two variables is statistically significant.

The chi-square hypothesis test used to evaluate categorical vs. categorical characteristics shows us that there is a significant difference in each characteristic with respect to our "co2_class" hazard class. We see that the most predominant class is “safe.” The characteristics “country” and “osmKey” are the ones that provide the most information to differentiate the classes; however, I consider that the characteristics ‘timeOfDay’ and “ventilation_type” are not negligible and can provide a differential, in addition to which I consider that the four categorical characteristics have a high relevance/importance due to the information they contain or allow us to analyze.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeikeer/IndoorCO2Map-Analysis/main/Results/Tables/chi_square_tests.png" alt="Table 4" width="600"/>
</p>

After an exhaustive study of characteristics, transformed and filtered, a list of the most relevant characteristics with greater separability for the $CO_2$ level class “co2_class” can be concluded:


| **Variable (Python name)** | **Description / Meaning**                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `co2readingsMed`           | Median of CO₂ readings during the measurement period. Represents the typical concentration level.               |
| `co2readingsStd`           | Standard deviation of CO₂ readings. Indicates the variability or fluctuations in concentration.                 |
| `co2readingsStd_diff`      | Standard deviation of consecutive CO₂ differences. Reflects short-term instability or oscillation.              |
| `timeOfDay`                | Classification of the measurement period based on time (Midnight, Morning, Noon, Afternoon).                    |
| `ventilation_type`         | Type of ventilation present in the location (natural, mechanical, or both active).                              |
| `countryName`              | Country where the measurement was recorded (only those with >10 valid records were analyzed).                   |
| `osmKey`                   | Key describing the type of establishment (e.g., restaurant, shop, office) according to OpenStreetMap tagging.   |
| `co2_class`                | CO₂ exposure risk classification based on ppm ranges (Safe, Moderate, High, etc.). Used as the main classifier. |

**Reference:** Table 5: Feature selection conclusions 

# Bibliography

- Akhter, F., Alahi, Md. E. E., Siddiquei, H. R., Gooneratne, C. P., & Mukhopadhyay, S. C. (2021). Graphene Oxide (GO) Coated Impedimetric Gas Sensor for Selective Detection of Carbon Dioxide (CO 2 ) With Temperature and Humidity Compensation. IEEE Sensors Journal, 21(4), 4241–4249. https://doi.org/10.1109/JSEN.2020.3035795

- Petersen, S., Jensen, K. L., Pedersen, A. L. S., & Rasmussen, H. S. (2016). The effect of increased classroom ventilation rate indicated by reduced CO2 concentration on the performance of schoolwork by children. Indoor Air, 26(3), 366–379. https://doi.org/10.1111/ina.12210
  
- WHN World Health Network. (2024, December). Indoor-CO2-Map: CO2 Monitoring and Data Collection. Https://Whn.Global/Indoor-Co2-Map-Co2-Monitoring-and-Data-Collection/.

- NASA, N. A. and S. A. (2025). Carbon Dioxide. https://svs.gsfc.nasa.gov/5115
  
- World Health Organization Regional Offi ce for Europe. (2010). SELECTED POLLUTANTS. WHO.https://whn.global/indoor-co2-map-co2-monitoring-and-data-collection/
