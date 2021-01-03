from utilities.math import isProb, combination, nProb
from utilities.util import isNegative


# negative binomial probability mass function P(x=i)
def negative_binomial_pmf(number_trials: int, probability: float, success: int = 1):
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability')

    combinations: float = combination(number_trials - 1, success - 1)
    prob_win: float = pow(probability, success)
    prob_lose: float = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


# negative binomial cumulative distribution function P(x<=i)
def negative_binomial_cdf(number_trials: int, probability: float, i: int = 1):
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while i >= 0:
        cumulating += negative_binomial_pmf(number_trials, probability, i)
        i -= 1

    return cumulating


# negative binomial probability mass function P(x=i)
def negative_binomial_pmf_R(probability: float, i: int):
    return i


# negative binomial distribution expected value
def negative_binomial_expected(probability: float, number_success: int) -> float:
    if not isProb(probability) or isNegative(number_success):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_success / probability


# negative binomial distribution variance
def negative_binomial_variance(probability: float, number_success: int) -> float:
    if not isProb(probability) or isNegative(number_success):
        raise ValueError('Invalid Parameter for probability or Number of Trials')
    return (number_success * nProb(probability)) / pow(probability, 2)


# print all data related to specific negative binomial distribution
def negative_binomial_all(number_trials: int, probability: float, success: int = 1, cumulative_i: int = 1):
    pmf: float = negative_binomial_pmf(number_trials, probability, success)
    cdf: float = negative_binomial_cdf(number_trials, probability, success)
    mean: float = negative_binomial_expected(probability, success)
    variance: float = negative_binomial_variance(probability, success)

    print(f"number of Trials = {number_trials}")
    print(f"probability = {probability}")
    print(f"success = {success}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")
