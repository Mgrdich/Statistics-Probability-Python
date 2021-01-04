from utilities.math import isProb, nProb
from utilities.util import isNegative, isZero


# geometric probability mass function P(x=i)
def geometric_pmf(probability: float, i: int) -> float:
    if not isProb(probability) or isNegative(i) or isZero(i):
        raise ValueError('Invalid Parameter for probability')
    q = pow(nProb(probability), i - 1)
    return q * probability


# geometric cumulative distribution function P(x<=i)
def geometric_cdf(probability: float, i: int) -> float:
    if not isProb(probability) or isNegative(i):
        raise ValueError('Invalid Parameter for probability')

    cumulating: float = 0
    while i > 0:  # distribution is not defined over 0
        cumulating += geometric_pmf(probability, i)
        i -= 1
    return cumulating


# geometric probability mass function P(x=i)
def geometric_pmf_R(probability: float, i: int) -> float:
    if not isProb(probability) or isNegative(i) or isZero(i):
        raise ValueError('Invalid Parameter for probability')

    if i == 1:  # initial case
        return geometric_pmf(probability, i)

    return nProb(probability) * geometric_pmf_R(probability, i - 1)


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


# print all data related to specific geometric distribution
def geometric_all(probability: float, success: int = 1, cumulative_i: int = 1):
    pmf: float = geometric_pmf(probability, success)
    cdf: float = geometric_cdf(probability, cumulative_i)
    mean: float = geometric_expected(probability)
    variance: float = geometric_variance(probability)

    print(f"probability = {probability}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")

# geometric_all(.5, 1, 6)
# print(geometric_pmf(.3, 9))
# print(geometric_pmf_R(.3, 9))
