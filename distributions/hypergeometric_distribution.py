# geometric probability mass function P(x=i)
def hyper_geometric_pmf(probability: float, i: int) -> float:
    return i


# geometric cumulative distribution function P(x<=i)
def hyper_geometric_cdf(probability: float, i: int) -> float:
    return i


# geometric distribution expected value
def hyper_geometric_expected() -> float:
    return 1


# geometric distribution variance
def hyper_geometric_variance() -> float:
    return 1


# print all data related to specific negative binomial distribution
def hyper_geometric_all(number_trials: int, probability: float, success: int = 1, cumulative_i: int = 1):
    pmf: float = hyper_geometric_pmf(number_trials, probability, success)
    cdf: float = hyper_geometric_cdf(number_trials, probability, cumulative_i)
    mean: float = hyper_geometric_expected()
    variance: float = hyper_geometric_variance()

    print(f"number of Trials = {number_trials}")
    print(f"probability = {probability}")
    print(f"success = {success}")

    print(f"P(X == {success}) = {pmf}")
    print(f"P(X <= {cumulative_i}) = {cdf}")
    print(f"E[X] = {mean}")
    print(f"Var(X) = {variance}")
