import sqlite3
import pandas as pd


path_db = "Python-OC-Lettings-FR/oc-lettings-site.sqlite3"
path_csv = "Python-OC-Lettings-FR/data_csv/"


def data_transfer(src, dst):
    # Extract :
    con = sqlite3.connect(path_db)
    data = pd.read_sql_query(f"SELECT * FROM {src}", con)
    con.close()

    # CSV naming
    name = src
    new = name.split('_')
    new_name = new[-1]
    csv = path_csv + f'{new_name}.csv'

    # Transform to CSV
    data.to_csv(csv, index=False)

    # Transfer to existing table
    con = sqlite3.connect(path_db)
    data = pd.read_csv(csv)
    data.to_sql(dst, con, if_exists='replace', index=False)
    con.close()


data_transfer('oc_lettings_site_address', 'lettings_address')
data_transfer('oc_lettings_site_profile', 'profiles_profile')
data_transfer('oc_lettings_site_letting', 'lettings_letting')
