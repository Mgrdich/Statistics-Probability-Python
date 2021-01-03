from utilities.math import isProb
from utilities.math import nProb
from utilities.math import isNegative


# geometric probability mass function P(x=i)
def geometric_pmf(probability: float, i: int) -> float:
    if not isProb(probability) or isNegative(i):
        raise ValueError('Invalid Parameter for probability')
    q = pow(nProb(probability), i - 1)
    return q * probability


# geometric cumulative distribution function P(x<=i)
def geometric_cdf(probability: float, i: int):
    if not isProb(probability) or isNegative(i):
        raise ValueError('Invalid Parameter for probability')

    cumulating: float = 0
    while i >= 0:
        cumulating += geometric_pmf(probability, i)
        i -= 1
    return cumulating


# geometric distribution expected value
def geometric_expected(probability: float) -> float:
    if not isProb(probability):
        raise ValueError('Invalid Parameter for probability')
    return 1 / probability


# geometric distribution variance
def geometric_variance(probability: float) -> float:
    if not isProb(probability):
        raise ValueError('Invalid Parameter for probability')
    return nProb(probability) / pow(probability, 2)
