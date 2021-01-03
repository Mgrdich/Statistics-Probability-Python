from utilities.math import isProb, combination, nProb
from utilities.util import isNegative


# negative binomial probability mass function P(x=i)
def negative_binomial_pmf(probability: float, success: int = 1, failures: int = 1):
    if not isProb(probability) or isNegative(failures) or isNegative(failures):
        raise ValueError('Invalid Parameter for probability')

    total_trial = success + failures

    combinations: float = combination(total_trial - 1, success - 1)
    prob_win: float = pow(probability, success)
    prob_lose: float = pow(nProb(probability), failures)
    return combinations * prob_win * prob_lose


# negative binomial cumulative distribution function P(x<=i)
def negative_binomial_cdf(probability: float, i: int = 1, failures: int = 1):
    if not isProb(probability) or isNegative(i) or isNegative(failures):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while i >= 0:
        cumulating += negative_binomial_pmf(probability, i, failures)
        i -= 1

    return cumulating


# negative binomial probability mass function P(x=i)
def negative_binomial_pmf_R(probability: float, success: int = 1, failures: int = 1):
    if not isProb(probability) or isNegative(failures) or isNegative(failures):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    total_trial = success + failures

    if success == 0:
        return pow(probability, success)

    x = total_trial * nProb(probability)
    y = failures + 1
    return negative_binomial_pmf_R(probability, success - 1, failures) * (x / y)


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


print(negative_binomial_pmf(.8, 5, 1))
print(negative_binomial_pmf_R(.8, 5, 1))
