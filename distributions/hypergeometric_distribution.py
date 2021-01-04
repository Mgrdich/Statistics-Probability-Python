from utilities.math import combination
from utilities.math import isNegative


# geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    valid2 = isNegative(number_white - total_chosen) or isNegative(success)
    if valid1 or valid2:
        raise ValueError('Invalid Parameter')

    x = combination(number_white, success) * combination(total_balls - number_white, total_chosen - success)
    y = combination(total_balls, total_chosen)
    return x / y


# geometric cumulative distribution function P(x<=i)
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


# geometric probability mass function P(x=i)
def hyper_geometric_pmf_R(probability: float, i: int) -> float:
    return i


# geometric distribution expected value
def hyper_geometric_expected(total_balls: int, total_chosen: int, number_white: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    if valid1 or isNegative(number_white - total_chosen):
        raise ValueError('Invalid Parameter')
    return (total_chosen * number_white) / total_balls


# geometric distribution variance
def hyper_geometric_variance(total_balls: int, total_chosen: int, number_white: int) -> float:
    valid1 = isNegative(total_chosen - total_chosen) or isNegative(total_balls - number_white)
    if valid1 or isNegative(number_white - total_chosen):
        raise ValueError('Invalid Parameter')

    p = number_white / total_balls
    x = total_chosen * p * (1 - p)
    y = 1 - ((total_chosen - 1) / (total_balls - 1))
    return x * y


# print all data related to specific negative binomial distribution
def hyper_geometric_all(total_trials: int, chosen_items: int, success: int = 1, cumulative_i: int = 1):
    pmf: float = hyper_geometric_pmf(total_trials, chosen_items, success)
    cdf: float = hyper_geometric_cdf(total_trials, chosen_items, cumulative_i)
    mean: float = hyper_geometric_expected()
    variance: float = hyper_geometric_variance()

    print(f"number of Trials N = {total_trials}")
    print(f"Chosen m = {chosen_items}")
    print(f"success = {success}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")
