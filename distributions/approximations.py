# poisson approximation binomial
from distributions.binomial_distribution import binomial_pmf, binomial_cdf
from distributions.poisson_distribution import poisson_pmf, poisson_cdf


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


# todo hyper geometric with the binomial
