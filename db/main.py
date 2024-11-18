import sqlite3
import csv

db = sqlite3.connect('../cars/tables/database.sqlite3')
cursor = db.cursor()

db.commit()
db.close()