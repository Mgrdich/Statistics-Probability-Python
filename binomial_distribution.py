from functions.math import combination


# binomial distribution probability mass function with parameter (number_trials, probability)
def binomial_pmf(number_trials: int, probability: float, success: int = 1) -> float:
    combinations = combination(number_trials, success)
    prob_win = pow(probability, success)
    prob_lose = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


# binomial distribution probability mass function with parameter (number_trials, probability)
def binomial_pmf_R(number_trials: int, probability: float, success: int = 0) -> float:
    success = success + 1
    p_over_np = (probability/1-probability)
    success_number_trials_mix = (number_trials-success/success+1)
    return p_over_np * success_number_trials_mix * binomial_pmf_R(number_trials, probability, (success - 1))


# binomial cumulative function P(x<=i)
def binomial_cdf(number_trials: int, probability: float, success: int = 1) -> float:
    return 1


print(binomial_pmf(5, 0.5, 0))
print(binomial_pmf_R(5, 0.5, 0))
