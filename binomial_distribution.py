from functions.math import combination
from functions.math import isProb
from functions.math import nProb


# binomial distribution probability mass function with parameter (number_trials, probability) p(i)
def binomial_pmf(number_trials: int, probability: float, success: int = 1) -> float:
    if not isProb(probability) or number_trials < 0:  # todo turn into a decorator
        raise ValueError('Invalid Parameter for probability')

    combinations = combination(number_trials, success)
    prob_win = pow(probability, success)
    prob_lose = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


# binomial distribution probability mass function with parameter (number_trials, probability) p(i)
def binomial_pmf_R(number_trials: int, probability: float, success: int = 0) -> float:
    if not isProb(probability) or number_trials < 0:  # todo turn into a decorator
        raise ValueError('Invalid Parameter for probability')

    success = success + 1  # todo starting initial case for recursion
    p_over_np = (probability / 1 - probability)
    success_number_trials_mix = (number_trials - success / success + 1)
    return p_over_np * success_number_trials_mix * binomial_pmf_R(number_trials, probability, (success - 1))


# binomial cumulative function P(x<=i)
def binomial_cdf(number_trials: int, probability: float, success: int = 1) -> float:
    if not isProb(probability) or number_trials < 0:  # todo turn into a decorator
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while success > 0:
        cumulating += binomial_pmf(number_trials, probability, success)
        success -= 1

    return cumulating


# expected value of a binomial distribution
def binomial_expected(number_trials: int, probability: float) -> float:
    if not isProb(probability) or number_trials < 0:  # todo turn into a decorator
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability


# variance of the expected value of binomial distribution
def binomial_variance(number_trials: int, probability: float) -> float:
    if not isProb(probability) or number_trials < 0:  # todo turn into a decorator
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability * nProb(probability)


print(binomial_pmf(5, 0.5, 0))
