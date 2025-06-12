# Question 4
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# This function should return a single number.

def answer_four():
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

    # Calculating the average for each country and sorting and getting the top 15 countries
    final["avgGDP"] = final[years].mean(axis=1)
    final = final.sort_values(by="avgGDP", ascending=False).head(15)

    # Calculating the GDP changed over the 10 year span for the country with the 6th largest average GDP
    GDP_change = final.iloc[5]
    GDP_change = GDP_change["2015"] - GDP_change["2006"]

    return GDP_change
