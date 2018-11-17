import sqlite3
import csv
from mystatsmodule import *


def main():
    with open('Universities.csv', "r") as cf:
        udataReader = csv.reader(cf)
        udata = list(udataReader)


    Median_SAT = [int(ud[2]) for ud in udata[1:]]
    accept_rate = [int(ud[3]) for ud in udata[1:]]
    exp_rate = [int(ud[4].replace(',', '')[1:]) for ud in udata[1:]]
    grad_rate = [int(ud[5]) for ud in udata[1:]]

    s1 = var_summary(Median_SAT)
    s2 = var_summary(accept_rate)
    s3 = var_summary(exp_rate)
    s4 = var_summary(grad_rate)

    median_SAT_std = [zscore(s1['avg'], s1['stdev'], x) for x in Median_SAT]
    accept_rate_std = [zscore(s2['avg'], s2['stdev'], x) for x in accept_rate]
    exp_rate_std = [zscore(s3['avg'], s3['stdev'], x) for x in exp_rate]
    grad_rate_std = [zscore(s4['avg'], s4['stdev'], x) for x in grad_rate]

    for i in range(len(udata)-1):
        if i == 0:
            udata[0].append("Median_SAT_STD")
            udata[0].append("Accept_rate_STD")
            udata[0].append("Exp_Rate_STD")
            udata[0].append("Grad_Rate_STD")
        else:
            udata[i].append(median_SAT_std[i])
            udata[i].append(accept_rate_std[i])
            udata[i].append(exp_rate_std[i])
            udata[i].append(grad_rate_std[i])


    # Print the result to a new csv
    with open('unistd.csv', "w") as cf:
        uwriter = csv.writer(cf,  lineterminator='\n')
        for row in udata:
            uwriter.writerow(row)


if __name__ == "__main__":
    main()
else:
    print("This module has not been designed to be called from other modules.")

DB_ = "ia04.sqlite"
CSV_ = "Universities.csv"

with open(CSV_ , "r") as fin:
	udataReader = csv.reader(fin)
	ud = list(udataReader)
	udata = []
	for row in ud[1:]:
		udata.append([str(row[0]), str(row[1]), int(row[2]), int(row[3]), int(row[4].replace(',', '')[1:]), int(row[5])])

conn=sqlite3.connect('DB_')
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS Universities")
cur.execute("CREATE TABLE Universities (School TEXT, Type TEXT, Median_SAT INTEGER, Acceptance_Rate_Perc INTEGER, Expenditures_per_Student INTEGER, Graduation_perc INTEGER);")
for row in udata:
	cur.execute("INSERT INTO Universities VALUES (?, ?, ?, ?, ?, ? )",  (row[0], row[1], row[2], row[3], row[4], row[5]))
conn.commit()
conn.close()

conn=sqlite3.connect('DB_')
cur = conn.cursor()
cur.execute("SELECT Median_SAT,  Acceptance_Rate_Perc, Expenditures_per_student," +
   "Graduation_perc FROM Universities ORDER BY School")
uddb = cur.fetchall()

Median_SAT  = [ud[0] for ud in uddb]
Acceptance_Rate_Perc = [ud[1] for ud in uddb]
Expenditures_per_student = [ud[2] for ud in uddb]
Graduation_perc = [ud[3] for ud in uddb]

s1 = var_summary(Median_SAT)
s2 = var_summary(Acceptance_Rate_Perc)
s3 = var_summary(Expenditures_per_student)
s4 = var_summary(Graduation_perc)

median_SAT_std = [zscore(s1['avg'], s1['stdev'], x) for x in Median_SAT]
Acceptance_Rate_Perc_std = [zscore(s2['avg'], s2['stdev'], x) for x in Acceptance_Rate_Perc]
Expenditures_per_student_std = [zscore(s3['avg'], s3['stdev'], x) for x in Expenditures_per_student]
Graduation_perc_std = [zscore(s4['avg'], s4['stdev'], x) for x in Graduation_perc]

conn = sqlite3.connect(DB_)
cur = conn.cursor()
cur.execute("ALTER TABLE Universities ADD  Median_SAT_std REAL")
cur.execute("ALTER TABLE Universities ADD  Acceptance_Rate_Perc_std REAL")
cur.execute("ALTER TABLE Universities ADD  Expenditures_per_student_std REAL")
cur.execute("ALTER TABLE Universities ADD  Graduation_perc_std REAL")
conn.commit()
conn.close()

conn = sqlite3.connect(DB_)
cur = conn.cursor()
for i in range(len(median_SAT_std)):
    cur.execute("UPDATE Universities SET Median_SAT_std = %s WHERE Median_SAT = %s " % (median_SAT_std[i],  median_SAT[i]))
conn.commit()
conn.close()

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
for i in range(len(Acceptance_Rate_Perc_std)):
    cur.execute("UPDATE Universities SET Acceptance_Rate_Perc_std = %s WHERE Acceptance_Rate_Perc = %s " % (Acceptance_Rate_Perc_std[i],  Acceptance_Rate_Perc[i]))
conn.commit()
conn.close()

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
for i in range(len(Graduation_perc_std)):
    cur.execute("UPDATE Universities SET Graduation_perc_std = %s WHERE Graduation_perc = %s " % (Graduation_perc_std[i],  Graduation_perc[i]))
conn.commit()
conn.close()
