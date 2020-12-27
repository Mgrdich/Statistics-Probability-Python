from functions.math import factorial
from functions.math import combination


# binomial distribution with parameter (number_trials, probability)
# trial tested size times
def binomial_distribution(number_trials: int, probability: float, tested: int = 1):
    success = 1
    combinations = combination(number_trials, success)
    prob_win = pow(probability, success)
    prob_lose = pow((1 - probability), (number_trials - success))
    return combinations * prob_win * prob_lose


print(binomial_distribution(5, 0.5, 0))
