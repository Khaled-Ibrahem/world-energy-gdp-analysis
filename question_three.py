# Question 3
# What are the top 15 countries for average GDP over the last 10 years?
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.

def answer_three():
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

    # Calculating the average for each country and sorting and getting the top 15 countries
    top_15["avgGDP"] = top_15[years].apply(lambda x: np.mean(x[years]),axis=1)
    avgGDP = top_15["avgGDP"].sort_values(ascending=False)
    
    return avgGDP
