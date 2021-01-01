from utilities.math import combination
from utilities.math import isProb
from utilities.math import nProb


# todo turn into a decorator all the validations of the utilities

# binomial distribution probability mass function with parameter (number_trials, probability) p(i)
def binomial_pmf(number_trials: int, probability: float, success: int = 1) -> float:
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability')

    combinations = combination(number_trials, success)
    prob_win = pow(probability, success)
    prob_lose = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


# binomial distribution probability mass function with parameter (number_trials, probability) p(i)
def binomial_pmf_R(number_trials: int, probability: float, success: int = 0) -> float:
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability')

    success = success + 1  # todo starting initial case for recursion
    p_over_np = (probability / 1 - probability)
    success_number_trials_mix = (number_trials - success / success + 1)
    return p_over_np * success_number_trials_mix * binomial_pmf_R(number_trials, probability, (success - 1))


# binomial cumulative function P(x<=i)
def binomial_cdf(number_trials: int, probability: float, i: int = 1) -> float:
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while i > 0:
        cumulating += binomial_pmf(number_trials, probability, i)
        i -= 1

    return cumulating


# expected value of a binomial distribution E[X]
def binomial_expected(number_trials: int, probability: float) -> float:
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability


# variance of the expected value of binomial distribution Var(X)
def binomial_variance(number_trials: int, probability: float) -> float:
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return number_trials * probability * nProb(probability)


# print all data related to specific binomial distribution
def binomial_all(number_trials: int, probability: float, success: int = 1, cumulative_i: int = 1):
    if not isProb(probability) or number_trials < 0:
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    pmf = binomial_pmf(number_trials, probability, success)
    cdf = binomial_cdf(number_trials, probability, cumulative_i)
    mean = binomial_expected(number_trials, probability)
    variance = binomial_variance(number_trials, probability)

    print("Number of Trials =", number_trials)
    print("p =", number_trials)

    print("P( X == ", success, ") = ", pmf)
    print("P( X <=", cumulative_i, ") =", cdf)
    print("E[X] =", mean)
    print("Var(X) =", variance)


# print(binomial_pmf(5, 0.5, 0))
# print(binomial_expected(5, 0.5))
# print(binomial_variance(5, 0.5))

binomial_all(10, 0.5, 2, 4)
