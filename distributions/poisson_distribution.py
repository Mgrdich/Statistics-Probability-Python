import math
from utilities.math import factorial
from utilities.util import isZero, isNegative


# todo  add print each P(X == i)

# poisson distribution probability mass function P(X = i) = p(i) i->success with parameter (param_lambda)
def poisson_pmf(param_lambda: float, success: int = 1) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    e_n_lambda: float = math.exp(-param_lambda)
    lambda_e_i: float = pow(param_lambda, success)
    return e_n_lambda * (lambda_e_i / factorial(success))


# poisson distribution probability mass function P(X = i) = p(i) i->success with parameter (param_lambda)
def poisson_pmf_R(param_lambda: float, success: int = 1) -> float:
    if isNegative(param_lambda):
        raise ValueError('Invalid Parameter for probability or Number of Trials')

    if isZero(success):  # initial case
        return poisson_pmf(param_lambda, success)

    return (param_lambda / success) * poisson_pmf_R(param_lambda, success - 1)


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
    cdf: float = poisson_cdf(param_lambda, cumulative_i)
    mean: float = poisson_expected(param_lambda)
    variance: float = poisson_variance(param_lambda)

    print(f"lambda = {param_lambda}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")


# poisson_all(3.2, 2, 2)
print(poisson_pmf(3.2, 8))
print(poisson_pmf_R(3.2, 8))
