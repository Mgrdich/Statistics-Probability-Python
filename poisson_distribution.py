import math
from utilities.math import factorial


# poisson distribution probability mass function p(i) i->success
def poisson_pmf(param_lambda: float, success: int) -> float:
    e_n_lambda: float = math.exp(-param_lambda)
    lambda_e_i: float = param_lambda ** success
    return e_n_lambda * (lambda_e_i / factorial(success))


# poisson cumulative distribution function P(x<=i)
def poisson_cdf(param_lambda: float, i: int = 1) -> float:
    cumulating: float = 0.0
    while i > 0:
        cumulating += poisson_pmf(param_lambda, i)
        i -= 1
    return cumulating


# poisson distribution expected value
def poisson_expected(param_lambda: float, success: int = 1) -> float:
    return 1


# poisson distribution variance
def poisson_variance(param_lambda: float, success: int = 1) -> float:
    return 1


# print all data related to specific poisson distribution
def poisson_all(param_lambda: float, success: int = 1, cumulative_i: int = 1):
    pmf: float = poisson_pmf(param_lambda, success)
    cdf: float = poisson_cdf(param_lambda, success)
    mean: float = poisson_expected(param_lambda, success)
    variance: float = poisson_variance(param_lambda, success)

    print(f"lambda = {param_lambda}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")
