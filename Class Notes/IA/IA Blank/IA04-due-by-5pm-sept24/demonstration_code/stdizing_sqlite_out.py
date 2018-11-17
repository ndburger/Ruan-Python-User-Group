""" Copy CSV into SQLite database, alter table, and insert standardize values.

Reads a csv files called universities.csv. Created database called IS04.sqlite
which contains standardized values for each of the 4 numeric types found within
universities.csv
"""

import csv
from mystatsmodule import *
import sqlite3

DB_NAME = "IA04.sqlite"
CSV_NAME = "universities.csv"

#def main():
""" Read all our data (remember, there's a header in this file)"""

# open and read csv file into udata
with open(CSV_NAME , "r") as cf:
    udataReader = csv.reader(cf)
    ud = list(udataReader)
    udata = []
    for row in ud[1:]:
        udata.append([str(row[0]), str(row[1]), int(row[2]), int(row[3]), int(row[4].replace(',', '')[1:]), int(row[5])])

# create database, table, and dump our udata into the table
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
# Create table
c.execute("DROP TABLE IF EXISTS universities")
c.execute("CREATE TABLE universities (School TEXT, Type TEXT, Median_SAT INTEGER, Acceptance_Rate_Perc INTEGER, Expenditures_per_student INTEGER, Graduation_perc INTEGER)")
for row in udata:
    c.execute("INSERT INTO universities VALUES (?, ?, ?, ?, ?, ? )",  (row[0], row[1], row[2], row[3], row[4], row[5]))  # Insert a row of data
conn.commit()
conn.close()


# load data from data base
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
c.execute("SELECT Median_SAT,  Acceptance_Rate_Perc, Expenditures_per_student," +
   "Graduation_perc FROM universities ORDER BY School") # The ORDER BY is IMPORTANT!
uddb = c.fetchall()


# read all columns into our variables
median_SAT  = [ud[0] for ud in uddb]
Acceptance_Rate_Perc = [ud[1] for ud in uddb]
Expenditures_per_student = [ud[2] for ud in uddb]
Graduation_perc = [ud[3] for ud in uddb]

# create a statistical summary of each variable
s1 = var_summary(median_SAT)
s2 = var_summary(Acceptance_Rate_Perc)
s3 = var_summary(Expenditures_per_student)
s4 = var_summary(Graduation_perc)

# standard the measures found within each variable
median_SAT_std = [zscore(s1['avg'], s1['stdev'], x) for x in median_SAT]
Acceptance_Rate_Perc_std = [zscore(s2['avg'], s2['stdev'], x) for x in Acceptance_Rate_Perc]
Expenditures_per_student_std = [zscore(s3['avg'], s3['stdev'], x) for x in Expenditures_per_student]
Graduation_perc_std = [zscore(s4['avg'], s4['stdev'], x) for x in Graduation_perc]

# Alter table
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
c.execute("ALTER TABLE universities ADD  Median_SAT_std REAL")
c.execute("ALTER TABLE universities ADD  Acceptance_Rate_Perc_std REAL")
c.execute("ALTER TABLE universities ADD  Expenditures_per_student_std REAL")
c.execute("ALTER TABLE universities ADD  Graduation_perc_std REAL")
conn.commit()
conn.close()

# insert into database values for Median_SAT_std
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
for i in range(len(median_SAT_std)):
    c.execute("UPDATE universities SET Median_SAT_std = %s WHERE Median_SAT = %s " % (median_SAT_std[i],  median_SAT[i]))
conn.commit()
conn.close()

# insert into database values for Acceptance_Rate_Perc_std
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
for i in range(len(Acceptance_Rate_Perc_std)):
    c.execute("UPDATE universities SET Acceptance_Rate_Perc_std = %s WHERE Acceptance_Rate_Perc = %s " % (Acceptance_Rate_Perc_std[i],  Acceptance_Rate_Perc[i]))
conn.commit()
conn.close()

# insert into database values for Expenditures_per_student_std
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
for i in range(len(Expenditures_per_student_std)):
    c.execute("UPDATE universities SET Expenditures_per_student_std = %s WHERE Expenditures_per_student = %s " % (Expenditures_per_student_std[i],  Expenditures_per_student[i]))
conn.commit()
conn.close()

# insert into database values for Graduation_perc_std
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
for i in range(len(Graduation_perc_std)):
    c.execute("UPDATE universities SET Graduation_perc_std = %s WHERE Graduation_perc = %s " % (Graduation_perc_std[i],  Graduation_perc[i]))
conn.commit()
conn.close()
