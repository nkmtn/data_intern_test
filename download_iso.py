import requests
import pandas as pd
from io import StringIO

resp = requests.get("https://gist.githubusercontent.com/richjenks/15b75f1960bc3321e295/raw/e9b473faed0c7512d6720d71d485b662cd743d25/countries.md", timeout=30)
df = pd.read_csv(StringIO(resp.text), sep='|')

NA = ['CA', 'US']

with open('iso_codes.csv', 'w', newline='') as file:
    df = df.sort_values(by=['Region'])
    for i, r in df.iterrows():
        if r["Region"] == "AMER":
            if r["ISO 3166"] in NA:
                df.at[i, 'Region'] = 'NAMER'
            else:
                df.at[i, 'Region'] = 'LATAM'

    df.to_csv('iso_codes.csv')


def print_all_region_codes():
    df = pd.read_csv('iso_codes.csv')
    s = ""
    for _, r in df.iterrows():
        s += "('" + str(r["ISO 3166"]) + "', '" + str(r["Region"]) + "'),"
    print("values for Region tables", s)


def print_list_of_country_codes():
    df = pd.read_csv('iso_codes.csv')
    s = ""
    for _, r in df.iterrows():
        s += "'%s'," % r["ISO 3166"]
    print("COUNTRY CODES: ", s)


REGIONS = ["APAC", "LATAM", "EMEA", "NAMER"]


def get_region_codes(region):
    df = pd.read_csv('iso_codes.csv')
    regions = df[df['Region'].str.startswith(region)]
    return list(regions["ISO 3166"])


print("APAC: ", get_region_codes("APAC"))
print("LATAM: ", get_region_codes("LATAM"))
print("EMEA: ", get_region_codes("EMEA"))
print("NA: ", get_region_codes("NAMER"))

print_list_of_country_codes()

print_all_region_codes()
