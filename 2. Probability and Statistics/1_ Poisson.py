'''
Write a Python function to calculate the probability of observing exactly k events in a fixed interval using the Poisson distribution formula. The function should take k (number of events) and lam (mean rate of occurrences) as inputs and return the probability rounded to 5 decimal places.
'''

import math

def poisson_probability(k, lam):
    """
    Calculate the probability of observing exactly k events in a fixed interval,
    given the mean rate of events lam, using the Poisson distribution formula.
    :param k: Number of events (non-negative integer)
    :param lam: The average rate (mean) of occurrences in a fixed interval
    """
    numerator = math.exp(-lam) * (lam ** k)
    denominator = math.factorial(k)
    prob = numerator / denominator
    
    return round(prob, 5)

k = 3
lam = 5
print(poisson_probability(k,lam))