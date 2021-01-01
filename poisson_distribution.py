import math
from utilities.math import factorial


# poisson distribution probability mass function p(i) i->success
def poisson_pmf(param_lambda: float, success: int) -> float:
    e_n_lambda = math.exp(-param_lambda)
    lambda_e_i = param_lambda ** success
    return e_n_lambda * (lambda_e_i / factorial(success))


# poisson cumulative distribution function P(x<=i)
def poisson_cdf(param_lambda: float,  success: int = 1) -> float:
    return 1


# poisson distribution expected value
def poisson_expected(param_lambda: float,  success: int = 1) -> float:
    return 1


# poisson distribution variance
def poisson_variance(param_lambda: float,  success: int = 1) -> float:
    return 1

# print all data related to specific poisson distribution
def poisson_all(param_lambda: float, success: int = 1,cumulative_i: int = 1):
    return 1