# Question 11
# Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample size (the number of countries in each continent bin),
# and the sum, mean, and std deviation for the estimated population of each country.
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']


def answer_eleven():
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
    Energy["Country"] = Energy["Country"].str.replace(r"\s*\(.*\)", "", regex=True)  # Remove parenthesis and contents
    Energy["Country"] = Energy["Country"].str.replace(r"\d+", "", regex=True)  # Remove any digits
    # Remove any extra spaces
    Energy["Country"] = Energy["Country"].str.strip()
    Energy["Country"] = Energy["Country"].replace(
        {
            "Republic of Korea": "South Korea", "United States of America": "United States", 
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", 
            "China, Hong Kong Special Administrative Region": "Hong Kong",
        }
    )

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
    df = pd.merge(ScimEn, Energy, how="inner", on="Country")
    df = pd.merge(df, GDP, how="inner", on="Country")
    df = df.set_index("Country").sort_values("Rank")
    top_15 = df[df["Rank"] <= 15]

     # estimate population of each country.
    top_15["Estimated Population"] = (
        top_15["Energy Supply"] / top_15["Energy Supply per Capita"]
    )

    # dictionary to group the Countries by Continent
    ContinentDict = {
        "China": "Asia",
        "United States": "North America",
        "Japan": "Asia",
        "United Kingdom": "Europe",
        "Russian Federation": "Europe",
        "Canada": "North America",
        "Germany": "Europe",
        "India": "Asia",
        "France": "Europe",
        "South Korea": "Asia",
        "Italy": "Europe",
        "Spain": "Europe",
        "Iran": "Asia",
        "Australia": "Australia",
        "Brazil": "South America",
    }

    # create a DataFrame that displays the sample size. the sum, mean, and std
    group = (
        top_15.groupby(ContinentDict)["Estimated Population"]
        .agg(["size", "sum", "mean", "std"])
        .rename_axis("Continent")
    )

    return group
