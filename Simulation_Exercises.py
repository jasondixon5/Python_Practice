import random
import numpy as np
"""
Experiment studied gender (male, female) and decision (promoted, not promoted)
n(male) = 24
n(female) = 24

order of columns is (promoted, not promoted)
order of rows is (male, female)
"""
#Index positions for references
promoted_idx = 0
not_promoted_idx = 1
male_idx = 0
female_idx = 1
male_observed = [21, 3]
female_observed = [14, 10]
n_male = sum(male_observed)
n_female = sum(female_observed)
observations = list(zip(male_observed, female_observed))


promotion_rate_male = observations[promoted_idx][male_idx] / n_male
promotion_rate_female = observations[promoted_idx][female_idx] / n_female

difference_promotion_rate_m2f = promotion_rate_male - promotion_rate_female

"""
Run a simulation of the male and female promotion rates received due to chance.
"""

simulation_n = n_male + n_female
simulation_male_n = sum(male_observed)
simulation_female_n = sum(female_observed)
simulation_promoted_n = sum(observations[promoted_idx])
simulation_not_promoted_n = sum(observations[not_promoted_idx])

simulated_results_promoted_female = 0
simulated_results_promoted_male = 0
simulated_results_not_promoted_female = 0
simulated_results_not_promoted_male = 0

"""
Given same number of promoted as originally observed, run simulation
Count how many female and how many male would be promoted by chance
"""
for _ in range(simulation_promoted_n):
    if random.random() < 0.5:
        simulated_results_promoted_female += 1
    else:
        simulated_results_promoted_male += 1

"""
Given same number of not promoted as originally observed, run simulation
Count how many female and how many male would not be promoted by chance
"""
        
for _ in range(simulation_not_promoted_n):
    if random.random() < 0.5:
        simulated_results_not_promoted_female += 1
    else:
        simulated_results_not_promoted_male += 1
        

assert (simulated_results_promoted_female + simulated_results_promoted_male) == simulation_promoted_n, "error in simulation promoted counts"

assert (simulated_results_not_promoted_female + simulated_results_not_promoted_male) == simulation_not_promoted_n, "error in simulation not promoted counts"

#Calculate simulated promotion and not promoted rates by gender
simulated_promoted_rate_female = simulated_results_promoted_female / simulation_promoted_n

simulated_promoted_rate_male = simulated_results_promoted_male / simulation_promoted_n

simulated_not_promoted_rate_female = simulated_results_not_promoted_female / simulation_not_promoted_n

simulated_not_promoted_rate_male = simulated_results_not_promoted_male / simulation_not_promoted_n

difference_in_simulated_promotion_rate_m2f = simulated_promoted_rate_male - simulated_promoted_rate_female

"""
Calculate difference between observed and simulated
i.e., difference between the difference between male and female promotion rates
"""
difference_observed_and_simulated = difference_promotion_rate_m2f - difference_in_simulated_promotion_rate_m2f

"""
Large simulation of above

"""

large_sim_diff_promo_rate_m2f = []

for _ in range(1000):
    simulated_results_promoted_female = 0
    simulated_results_promoted_male = 0
    
    for _ in range(simulation_promoted_n):
        if random.random() < 0.5:
            simulated_results_promoted_female += 1
        else:
            simulated_results_promoted_male += 1
    
    simulated_promoted_rate_female = simulated_results_promoted_female / simulation_promoted_n
    
    simulated_promoted_rate_male = simulated_results_promoted_male / simulation_promoted_n
    
    diff_in_simulated_promotion_rate_m2f = simulated_promoted_rate_male - simulated_promoted_rate_female
    
    large_sim_diff_promo_rate_m2f.append(diff_in_simulated_promotion_rate_m2f)
