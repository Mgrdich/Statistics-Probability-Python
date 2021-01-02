import math
from utilities.math import factorial
from distributions.binomial_distribution import binomial_pmf
from distributions.binomial_distribution import binomial_cdf
from utilities.util import isNegative


# todo  add print each P(X == i)

# poisson distribution probability mass function P(X = i) = p(i) i->success with parameter (param_lambda)
def poisson_pmf(param_lambda: float, success: int) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    e_n_lambda: float = math.exp(-param_lambda)
    lambda_e_i: float = param_lambda ** success
    return e_n_lambda * (lambda_e_i / factorial(success))


# poisson distribution probability mass function P(X = i) = p(i) i->success with parameter (param_lambda)
def poisson_pmf_R(param_lambda: float, success: int) -> float:
    return 1


# poisson cumulative distribution function P(x<=i)
def poisson_cdf(param_lambda: float, i: int = 1) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    cumulating: float = 0.0
    while i >= 0:
        cumulating += poisson_pmf(param_lambda, i)
        i -= 1
    return cumulating


# poisson distribution expected value
def poisson_expected(param_lambda: float) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return param_lambda


# poisson distribution variance
def poisson_variance(param_lambda: float) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    return param_lambda ** 2


# print all data related to specific poisson distribution
def poisson_all(param_lambda: float, success: int = 1, cumulative_i: int = 1):
    pmf: float = poisson_pmf(param_lambda, success)
    cdf: float = poisson_cdf(param_lambda, success)
    mean: float = poisson_expected(param_lambda)
    variance: float = poisson_variance(param_lambda)

    print(f"lambda = {param_lambda}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")


# poisson approximation binomial
def poisson_approximate_binomial(number_trials: int, probability: float, param_lambda: float, success: int):
    pmf_poisson: float = poisson_pmf(param_lambda, success)
    cdf_poisson: float = poisson_cdf(param_lambda, success)
    pmf_binomial: float = binomial_pmf(number_trials, probability, success)
    cdf_binomial: float = binomial_cdf(number_trials, probability, success)
    error_margin_pmf: float = abs(pmf_poisson - pmf_binomial)
    error_margin_cdf: float = abs(cdf_poisson - cdf_binomial)
    print(f"Poisson P(X == {success}) = {pmf_poisson}")
    print(f"Poisson P(X <= {success}) = {cdf_poisson}")
    print(f"Binomial P(X == {success}) = {pmf_binomial}")
    print(f"Binomial P(X <= {success}) = {cdf_binomial}")
    print(f"Error Margin PMF = {error_margin_pmf}")
    print(f"Error Margin CDF = {error_margin_cdf}")


# poisson_approximate_binomial(10, 0.1, 1, 1)
poisson_all(3.2, 2, 2)
