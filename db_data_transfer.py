import sqlite3
import sys

def open_db():
    con = sqlite3.connect('oc-lettings-site.sqlite3')
    cur = con.cursor()