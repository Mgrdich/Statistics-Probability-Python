from utilities.math import combination
from utilities.util import isNegative


# hyper geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    not_valid1 = isNegative(total_chosen - total_chosen)
    limit = max(0, total_chosen - total_balls + number_white)
    valid2 = limit <= success <= min(total_chosen, number_white)

    if not_valid1 or not valid2:
        raise ValueError('Invalid Parameter')

    x = combination(number_white, success) * combination(total_balls - number_white, total_chosen - success)
    y = combination(total_balls, total_chosen)
    return x / y


# hyper geometric cumulative distribution function P(x<=i)
def hyper_geometric_cdf(total_balls: int, total_chosen: int, number_white: int, i: int) -> float:
    not_valid1 = isNegative(total_chosen - total_chosen)
    limit = max(0, total_chosen - total_balls + number_white)
    valid2 = limit <= i <= min(total_chosen, number_white)

    if not_valid1 or not valid2:
        raise ValueError('Invalid Parameter')

    cumulating: float = 0.0
    while i >= limit:
        cumulating += hyper_geometric_pmf(total_balls, total_chosen, number_white, i)
        i -= 1

    return cumulating


# hyper geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf_R(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    not_valid1 = isNegative(total_chosen - total_chosen)
    limit = max(0, total_chosen - total_balls + number_white)
    valid2 = limit <= success <= min(total_chosen, number_white)

    if not_valid1 or not valid2:
        raise ValueError('Invalid Parameter')

    if success == limit:
        return hyper_geometric_pmf(total_balls, total_chosen, number_white, success)

    success -= 1
    x = (number_white - success) * (total_chosen - success)
    y = (1 + success) * (1 - number_white + total_balls - total_chosen + success)
    return (x / y) * hyper_geometric_pmf_R(total_balls, total_chosen, number_white, success)


# hyper geometric distribution expected value
def hyper_geometric_expected(total_balls: int, total_chosen: int, number_white: int) -> float:
    not_valid1 = isNegative(total_balls - total_chosen)
    if not_valid1:
        raise ValueError('Invalid Parameter')

    return (total_chosen * number_white) / total_balls


# hyper geometric distribution variance
def hyper_geometric_variance(total_balls: int, total_chosen: int, number_white: int) -> float:
    not_valid1 = isNegative(total_chosen - total_chosen)
    if not_valid1:
        raise ValueError('Invalid Parameter')

    p = number_white / total_balls
    x = total_chosen * p * (1 - p)
    y = 1 - ((total_chosen - 1) / (total_balls - 1))
    return x * y


# print all data related to specific hyper geometric distribution
def hyper_geometric_all(total_balls: int, total_chosen: int, number_white: int, success: int, cumulative_i: int = 1):
    not_valid1 = isNegative(total_balls - total_chosen)
    limit = max(0, total_chosen - total_balls + number_white)
    valid2 = limit <= success <= min(total_chosen, number_white)

    if not_valid1 or not valid2:
        raise ValueError('Invalid Parameter')

    pmf: float = hyper_geometric_pmf(total_balls, total_chosen, number_white, success)
    cdf: float = hyper_geometric_cdf(total_balls, total_chosen, number_white, cumulative_i)
    mean: float = hyper_geometric_expected(total_balls, total_chosen, number_white)
    variance: float = hyper_geometric_variance(total_balls, total_chosen, number_white)

    print(f"number of Balls N = {total_balls}")
    print(f"m white = {number_white}")
    print(f"n choosing = {total_chosen}")
    print(f"success = {success}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")


print(hyper_geometric_pmf(10, 7, 4, 2))
print(hyper_geometric_cdf(10, 7, 4, 2))
