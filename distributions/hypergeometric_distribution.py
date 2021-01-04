from utilities.math import combination
from utilities.util import isNegative


# hyper geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    valid2 = isNegative(number_white - total_chosen) or isNegative(success)
    if valid1 or valid2:
        raise ValueError('Invalid Parameter')

    x = combination(number_white, success) * combination(total_balls - number_white, total_chosen - success)
    y = combination(total_balls, total_chosen)
    return x / y


# hyper geometric cumulative distribution function P(x<=i)
def hyper_geometric_cdf(total_balls: int, total_chosen: int, number_white: int, i: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    valid2 = isNegative(number_white - total_chosen) or isNegative(i)
    if valid1 or valid2:
        raise ValueError('Invalid Parameter')

    cumulating: float = 0.0
    while i >= 0:
        cumulating += hyper_geometric_pmf(total_balls, total_chosen, number_white, i)
        i -= 1

    return cumulating


# hyper geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf_R(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    valid2 = isNegative(number_white - total_chosen) or isNegative(success)
    if valid1 or valid2:
        raise ValueError('Invalid Parameter')

    if success == 0:
        return hyper_geometric_pmf(total_balls, total_chosen, number_white, success)

    x = (number_white - success) * (total_chosen - success)
    y = (1 + success) * (1 - number_white + total_balls - total_chosen + success)
    return (x / y) * hyper_geometric_pmf_R(total_balls, total_chosen, number_white, success - 1)


# hyper geometric distribution expected value
def hyper_geometric_expected(total_balls: int, total_chosen: int, number_white: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    if valid1 or isNegative(number_white - total_chosen):
        raise ValueError('Invalid Parameter')
    return (total_chosen * number_white) / total_balls


# hyper geometric distribution variance
def hyper_geometric_variance(total_balls: int, total_chosen: int, number_white: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    if valid1 or isNegative(number_white - total_chosen):
        raise ValueError('Invalid Parameter')

    p = number_white / total_balls
    x = total_chosen * p * (1 - p)
    y = 1 - ((total_chosen - 1) / (total_balls - 1))
    return x * y


# print all data related to specific hyper geometric distribution
def hyper_geometric_all(total_balls: int, total_chosen: int, number_white: int, success: int, cumulative_i: int = 1):
    pmf: float = hyper_geometric_pmf(total_balls, total_chosen, number_white, success)
    cdf: float = hyper_geometric_cdf(total_balls, total_chosen, number_white, cumulative_i)
    mean: float = hyper_geometric_expected()
    variance: float = hyper_geometric_variance()

    print(f"number of Balls N = {total_balls}")
    print(f"m white = {number_white}")
    print(f"n choosing = {total_chosen}")
    print(f"success = {success}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")
