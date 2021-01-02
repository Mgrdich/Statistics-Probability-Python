from utilities.math import combination
from utilities.math import isProb
from utilities.math import nProb
from utilities.util import isNegative
from utilities.util import isZero


# todo turn into a decorator all the validations of the utilities
# todo  add print each P(X == i)

# binomial distribution probability mass function P(X = i) = p(i) with parameter (number_trials, probability) p(i)
def binomial_pmf(number_trials: int, probability: float, success: int = 1) -> float:
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability')

    combinations: float = combination(number_trials, success)
    prob_win: float = pow(probability, success)
    prob_lose: float = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


# binomial distribution probability mass function P(X = i) = p(i) with parameter (number_trials, probability) p(i)
def binomial_pmf_R(number_trials: int, probability: float, success: int = 1) -> float:
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability')

    if isZero(success):  # initial case
        return binomial_pmf(number_trials, probability, success)

    p_over_np: float = (probability / 1 - probability)
    success_number_trials_mix: float = (number_trials - success / success + 1)
    return p_over_np * success_number_trials_mix * binomial_pmf_R(number_trials, probability, (success - 1))


# binomial cumulative function P(x<=i)
def binomial_cdf(number_trials: int, probability: float, i: int = 1) -> float:
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while i >= 0:
        cumulating += binomial_pmf(number_trials, probability, i)
        i -= 1

    return cumulating


# expected value of a binomial distribution E[X]
def binomial_expected(number_trials: int, probability: float) -> float:
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability


# variance of the expected value of binomial distribution Var(X)
def binomial_variance(number_trials: int, probability: float) -> float:
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability * nProb(probability)


# print all data related to specific binomial distribution
def binomial_all(number_trials: int, probability: float, success: int = 1, cumulative_i: int = 1):
    if not isProb(probability) or isNegative(number_trials):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    pmf: float = binomial_pmf(number_trials, probability, success)
    cdf: float = binomial_cdf(number_trials, probability, cumulative_i)
    mean: float = binomial_expected(number_trials, probability)
    variance: float = binomial_variance(number_trials, probability)

    print(f"Number of Trials = {number_trials}")
    print(f"p = {probability}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")

# print(binomial_pmf(10, 0.5, 0))
# print(binomial_pmf(10, 0.5, 0) == binomial_pmf_R(10, 0.5, 0))
# print(binomial_expected(5, 0.5))
# print(binomial_variance(5, 0.5))

# binomial_all(100, 0.75, 70, 70)

# print(binomial_pmf_R(10, 0.5, 0))
