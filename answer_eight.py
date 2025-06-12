# Question 8
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?
# This function should return the name of the country

def answer_eight():
    import numpy as np
    import pandas as pd

    # Reading the energy supply and renewable electricity production file and Removing all unneccessary columns and rows
    Energy = pd.read_excel(
        "assets/Energy Indicators.xls",
        skiprows=18,
        skipfooter=38,
        na_values=["..."],
        header=None,
        names=[
            "a",
            "b",
            "Country",
            "Energy Supply",
            "Energy Supply per Capita",
            "% Renewable",
        ],
    )
    Energy = Energy.drop(["a", "b"], axis=1)

    # Converting Energy Supply to gigajoules instead of petajoule
    Energy["Energy Supply"] = Energy["Energy Supply"] * 1000000

    # Cleaning the data to be ready to use
    Energy["Country"] = Energy["Country"].replace(
        {
            "Republic of Korea": "South Korea",
            "United States of America20": "United States",
            "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
            "China, Hong Kong Special Administrative Region3": "Hong Kong",
        }
    )

    Energy["Country"] = Energy["Country"].str.replace(
        r"\s*\(.*\)", "", regex=True
    )  # Remove parenthesis and contents
    Energy["Country"] = Energy["Country"].str.replace(
        r"\d+", "", regex=True
    )  # Remove any digits
    # Remove any extra spaces
    Energy["Country"] = Energy["Country"].str.strip()

    # Reading the  Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology file
    ScimEn = pd.read_excel("assets/scimagojr-3.xlsx")

    # Reading the GDP data file and removing the unneccessary rows
    GDP = pd.read_csv("assets/world_bank.csv", skiprows=4)

    # Renaming the country
    GDP = GDP.rename(columns={"Country Name": "Country"})
    GDP["Country"] = GDP["Country"].replace(
        {
            "Korea, Rep.": "South Korea",
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong",
        }
    )
    years = [str(year) for year in range(2006, 2016)]
    GDP = GDP[["Country"] + years]

    # Join the three datasets: GDP, Energy, and ScimEn into a new dataset and modify it
    final = pd.merge(ScimEn, Energy, how="inner", on="Country")
    final = pd.merge(final, GDP, how="inner", on="Country")
    final = final.set_index("Country")

    # Estimating the population and getting the third country
    final["Estimated Population"] = (
        final["Energy Supply"] / final["Energy Supply per Capita"]
    )
    third_populous_country = (
        final.sort_values(by="Estimated Population",
                          ascending=False).iloc[2].name
    )

    return third_populous_country
