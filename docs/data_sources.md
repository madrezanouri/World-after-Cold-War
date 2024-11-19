# Dataset Documentation

## Overview
This project analyzes global economic and demographic trends since 1991, using data from a variety of trusted sources. Below, you'll find detailed information on each dataset, including its source, format, and key features.

---

## Data Sources
1. **Economic Indicators**  
   - **Sources**: World Bank Open Data ([https://data.worldbank.org](https://data.worldbank.org))
     .Trading Econimics ([https://tradingeconomics.com/united-states/indicators])
                  International Monetary Fund ([(https://www.imf.org/en/Home)])
                  Macrotrends ([https://www.macrotrends.net/])
                  Ycharts ([https://ycharts.com/])
                  CEIC Data ([https://www.ceicdata.com/])
                  Moody's Analytics ([https://www.economy.com/])
                  Federal Reserve Bank of ST. Louis ([https://fred.stlouisfed.org/])
                  Mortgage Strategy ([https://www.mortgagestrategy.co.uk/])
                  FXempire ([https://www.fxempire.com/])
                  CIA ([https://www.cia.gov/])
                  
                 
   - **Description**: Contains data on GDP Growth Rate, Inflation Rate, Debt-to-GDP Ratio, and Net Exports.  
   - **Format**: CSV  ,  xlsx
   - **Notes**: Raw data was cleaned and processed to ensure consistency across years and countries.  

2. **Population Indicators**  
   - **Sources**: United Nations Department of Economic and Social Affairs ([https://www.un.org/development/desa]](https://population.un.org/))
                  Worldometer ([https://www.worldometers.info/])
     
   - **Description**: Provides data on Total Population, Population Growth Rate, Fertility Rate, and Net Migration.  
   - **Format**: Excel  
   - **Notes**: Missing values for certain countries were imputed using regional averages.  

3. **Country-Specific Data**  
   - **Sources**: US Bureau of Labor Statistics ([https://www.bls.gov](https://www.bls.gov))
                  Fiscal Data ([(https://fiscaldata.treasury.gov])
                  US Inflation Calculator ([https://www.usinflationcalculator.com/])
                  US Bureau of Economic Analysis ([https://www.bea.gov/])
                  Deutsche Bundesbank Eurosystem ([https://www.bundesbank.de/])
                  Office for National Statistics UK ([https://www.ons.gov.uk/])
                  Banque de France ([https://www.banque-france.fr/])
                  Reserve Bank of Australia ([https://www.rba.gov.au/])
     
   - **Description**: Supplementary data for unemployment and labor participation rates.  
   - **Format**: CSV and Excel  
   - **Notes**: Integrated into the master dataset after harmonization with global datasets.

---

## Preprocessing Steps
1. **Raw Data Cleaning**:
   - Standardized column names across all datasets.
   - Removed duplicate entries and inconsistent formatting.
2. **Merging Datasets**:
   - Merged datasets by `Country` and `Year`.
   - Handled missing values through imputation or interpolation where necessary.
3. **Processed Output**:
   - Final dataset saved as `data/processed/master_data.csv` with 10 countries and 30+ years of data.

---

## Key Indicators and Their Sources
| Indicator                      | Source                          | Description                                             |
|--------------------------------|---------------------------------|---------------------------------------------------------|
| GDP Growth Rate                | World Bank                     | Annual percentage growth of GDP.                       |
| Inflation Rate                 | World Bank                     | Consumer price inflation (annual %).                   |
| Unemployment                   | US Bureau of Labor Statistics  | Percentage of the labor force unemployed.              |
| Population Growth Rate         | United Nations                 | Annual growth rate of the population.                  |
| Total Population               | United Nations                 | Total population for each country.                     |
| Central Government Debt-to-GDP | IMF                            | Ratio of government debt to GDP.                       |

---

## Additional Notes
- Data for certain countries and years was missing. These gaps were addressed through:
  - Extrapolation using trends from neighboring countries.
  - Imputation with regional or global averages.
- Some indicators (e.g., Net Exports) were scaled to ensure comparability across countries.

---

## References
- World Bank Open Data: [https://data.worldbank.org](https://data.worldbank.org)  
- United Nations: [https://www.un.org/development/desa](https://www.un.org/development/desa)  
- US Bureau of Labor Statistics: [https://www.bls.gov](https://www.bls.gov)  
- International Monetary Fund: [https://www.imf.org](https://www.imf.org)  

