from utilities.math import combination


# geometric probability mass function P(x=i) (N,m,n) N->total_trials m->number_white n->total chosen
def hyper_geometric_pmf(total_balls: int, total_chosen: int, number_white: int, success: int) -> float:
    x = combination(number_white, success) * combination(total_balls - number_white, total_chosen - success)
    y = combination(total_balls, total_chosen)
    return x / y


# geometric cumulative distribution function P(x<=i)
def hyper_geometric_cdf(probability: float, i: int) -> float:
    return i


# geometric probability mass function P(x=i)
def hyper_geometric_pmf_R(probability: float, i: int) -> float:
    return i


# geometric distribution expected value
def hyper_geometric_expected(total_balls: int, total_chosen: int, number_white: int) -> float:
    return (total_chosen * number_white) / total_balls


# geometric distribution variance
def hyper_geometric_variance(total_balls: int, total_chosen: int, number_white: int) -> float:
    p = number_white / total_balls
    x = total_chosen * p * (1 - p)
    y = 1 - ((total_chosen - 1)/(total_balls-1))
    return x*y


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
