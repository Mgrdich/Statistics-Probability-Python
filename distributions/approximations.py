from distributions.binomial_distribution import binomial_pmf, binomial_cdf
from distributions.poisson_distribution import poisson_pmf, poisson_cdf
from distributions.hypergeometric_distribution import hyper_geometric_pmf, hyper_geometric_cdf


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


# hyper geometric approximation binomial
def hyper_geometric_binomial(total_balls: int, total_chosen: int, number_white: int, success: int):

    pmf_hyper_geometric: float = hyper_geometric_pmf(total_balls, total_chosen, number_white, success)
    cdf_hyper_geometric: float = hyper_geometric_cdf(total_balls, total_chosen, number_white, success)

    p = number_white / total_balls
    cdf_binomial: float = binomial_cdf(total_chosen, p, success)
    pmf_binomial: float = binomial_pmf(total_chosen, p, success)

    error_margin_pmf: float = abs(pmf_binomial - pmf_hyper_geometric)
    error_margin_cdf: float = abs(cdf_binomial - cdf_hyper_geometric)

    print(f"Hyper Geometric P(X == {success}) = {pmf_hyper_geometric}")
    print(f"Hyper Geometric P(X <= {success}) = {cdf_hyper_geometric}")
    print(f"Binomial P(X == {success}) = {pmf_binomial}")
    print(f"Binomial P(X <= {success}) = {cdf_binomial}")
    print(f"Error Margin PMF = {error_margin_pmf}")
    print(f"Error Margin CDF = {error_margin_cdf}")


# poisson_approximate_binomial(10, 0.1, 1, 1)
hyper_geometric_binomial(100000, 99000, 4, 2)
