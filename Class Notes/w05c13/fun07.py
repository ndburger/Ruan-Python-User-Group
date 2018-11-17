"""Demonstration of standardizing values"""


import csv


def var_summary(x):
    maxx = max(x)
    minx = min(x)
    n = len(x)
    sum_x = sum(x)
    avg = sum_x / n
    deviations = [(a - avg)**2 for a in x]
    variation = sum(deviations)/n
    std_deviation = variation ** .5
    return({'max': maxx, 'min': minx, 'n': n, 'sum': sum_x,
            'avg': avg, 'variance': variation, 'stdev': std_deviation})


def zscore(avg, stdev, x):
    return((x-avg)/stdev)

with open('univerisities.csv', "r") as cf:
    unidata = csv.reader(cf)

print(unidata)
type(unidata)

"""
summary = var_summary(unidata[3])
summary = var_summary(unidata[4])
summary = var_summary(unidata[5])
summary = var_summary(unidata[6])

print(summary)
print("zscore x1 = ", zscore(summary['avg'], summary['stdev'], x[0]))
print("zscore x2 = ", zscore(summary['avg'], summary['stdev'], x[1]))
print("zscore x3 = ", zscore(summary['avg'], summary['stdev'], x[2]))
print("zscore x4 = ", zscore(summary['avg'], summary['stdev'], x[3]))
print("zscore x5 = ", zscore(summary['avg'], summary['stdev'], x[4]))
"""
