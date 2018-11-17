"""Statistics module to calculate statistical summary and zscore."""


def var_summary(x):
    """Return a statistical summary of a given list of values."""
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
    """Calculate a standardized value, or zscore, for x given avg and stdev."""
    return((x-avg)/stdev)
