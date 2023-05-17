import sqlite3
import pandas as pd

'''
def open_db():
    con = sqlite3.connect('Python-OC-Lettings-FR/oc-lettings-site.sqlite3')
    cur = con.cursor()

    # To add > Create folder data
    path = 'Python-OC-Lettings-FR/data_csv'
    os.makedirs(path, exist_ok=True)


    data1 = cur.execute("SELECT * FROM oc_lettings_site_address")
    with open('Python-OC-Lettings-FR/data_csv/adresses.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data1)

    data2 = cur.execute("SELECT * FROM oc_lettings_site_profile")
    with open('Python-OC-Lettings-FR/data_csv/profiles.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data2)

    data3 = cur.execute("SELECT * FROM oc_lettings_site_letting")
    with open('Python-OC-Lettings-FR/data_csv/lettings.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data3)

    data4 = cur.execute("SELECT * FROM auth_user")
    with open('Python-OC-Lettings-FR/data_csv/users.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data4)

def copy_csv_to_table():

    data1 = pd.read_csv('Python-OC-Lettings-FR/data_csv/adresses.csv',
                        names=["id",
                               "number",
                               "street",
                               "city",
                               "state",
                               "zip_code",
                               "country_iso_code"],)

    con = sqlite3.connect('Python-OC-Lettings-FR/oc-lettings-site.sqlite3')
    data1.to_sql('lettings_address', con, index=False, if_exists='replace')


    con.close()

def show_tables():
    con = sqlite3.connect('Python-OC-Lettings-FR/oc-lettings-site.sqlite3')
    print("Connexion établie avec la base de données")
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print(tables)
    for table in tables:
        print(table[0])
    con.close()

show_tables()
open_db()
copy_csv_to_table()
'''
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
