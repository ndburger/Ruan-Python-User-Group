""" Method to standardize values read, and added back, to a csv file.

Reads a csv files called universities.csv. Outputs a file called unistd.csv
which contains standardized values for each of the 4 numeric types found within
universities.csv
"""

import csv
from mystatsmodule import *


def main():
    """ Read all our data (remember, there's a header in this file)"""
    with open('universities.csv', "r") as cf:
        udataReader = csv.reader(cf)
        udata = list(udataReader)

    # read all columns into our variables
    median_SAT = [int(ud[2]) for ud in udata[1:]]
    accept_rate = [int(ud[3]) for ud in udata[1:]]
    exp_rate = [int(ud[4].replace(',', '')[1:]) for ud in udata[1:]]
    grad_rate = [int(ud[5]) for ud in udata[1:]]

    # create a statistical summary of each variable
    s1 = var_summary(median_SAT)
    s2 = var_summary(accept_rate)
    s3 = var_summary(exp_rate)
    s4 = var_summary(grad_rate)

    # standard the measures found within each variable
    median_SAT_std = [zscore(s1['avg'], s1['stdev'], x) for x in median_SAT]
    accept_rate_std = [zscore(s2['avg'], s2['stdev'], x) for x in accept_rate]
    exp_rate_std = [zscore(s3['avg'], s3['stdev'], x) for x in exp_rate]
    grad_rate_std = [zscore(s4['avg'], s4['stdev'], x) for x in grad_rate]

    # assemble our datastructure into rows for writing
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
