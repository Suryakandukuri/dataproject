# %%
# importing the library
import pandas as pd

# %%
# reading the data from csv files to create dataframes
who_data = pd.read_csv("data/who_dataset.csv")
covid_data = pd.read_csv("data/country_wise_latest.csv")
# %%
# limiting the WHO dataset with a few columns
# that could be relevant to health domain personnel
who_data = who_data[
    [
        "country",
        "population_in_thousands_total",
        "community_and_traditional_health_workers_density_per_10_000_population",
        "environment_and_public_health_workers_density_per_10_000_population",
        "hospital_beds_per_10_000_population",
        "laboratory_health_workers_density_per_10_000_population",
        "number_of_community_and_traditional_health_workers",
        "number_of_laboratory_health_workers",
        "number_of_nursing_and_midwifery_personnel",
        "number_of_physicians",
        "number_of_other_health_service_providers"
    ]
]
# %%
# merge the two dataframe
covid_who = covid_data.merge(who_data, how= "inner", left_on='Country/Region', right_on='country')
# %%
# creating another column to calculate total healthcare personnel
covid_who["total_healthcare_personnel"] = covid_who.iloc[:, -4:-1].sum(axis=1)
# %%
# creating a column recovered_percent
covid_who["recovered_percent"] = (covid_who["Recovered"]/covid_who["Confirmed"])*100
# %%
