import requests
import pandas as pd
from io import StringIO

REGIONS = ["APAC", "LATAM", "EMEA", "NAMER"]


def download_list():
    resp = requests.get(
        "https://gist.githubusercontent.com/richjenks/15b75f1960bc3321e295/raw/e9b473faed0c7512d6720d71d485b662cd743d25/countries.md",
        timeout=30)
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


def print_region_table():
    df = pd.read_csv('iso_codes.csv')
    s = ""
    for _, r in df.iterrows():
        s += "('" + str(r["ISO 3166"]) + "', '" + str(r["Region"]) + "'),"
    print("Values for Region tables", s)


def print_list_of_country_codes():
    df = pd.read_csv('iso_codes.csv')
    s = ""
    for _, r in df.iterrows():
        s += "'%s'," % r["ISO 3166"]
    print("COUNTRY CODES: \n", s)


def get_region_codes(region):
    df = pd.read_csv('iso_codes.csv')
    regions = df[df['Region'].str.startswith(region)]
    return list(regions["ISO 3166"])


def print_codes_by_regions():
    print("Codes per region \n")
    for r in REGIONS:
        if r == "NAMER":
            print("NA: \n", get_region_codes(r))
            continue
        print("%s: \n" % r, get_region_codes(r))


download_list()
print_list_of_country_codes()
print_region_table()
print_codes_by_regions()
