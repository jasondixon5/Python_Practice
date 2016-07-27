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


male_promotion_rate = observations[promoted_idx][male_idx] / n_male
female_promotion_rate = observations[promoted_idx][female_idx] / n_female

promotion_rate_difference = male_promotion_rate - female_promotion_rate

"""
Run a simulation of the male and female promotion rates received due to chance.
"""

simulation_n = n_male + n_female
simulation_male_n = sum(male_observed)
simulation_female_n = sum(female_observed)
simulation_promoted_n = sum(observations[promoted_idx])
simulation_not_promoted_n = sum(observations[not_promoted_idx])

#Count number of female promotions in one random simulation (as test)
simulated_female_promotions = sum(1 if random.random() < 0.5 else 0 for _ in range(simulation_female_n))

#Count number of male promotions in one random simulation (as test)
simulated_male_promotions = sum(1 if random.random() < 0.5 else 0 for _ in range(simulation_male_n))

#Calculate female promotion rate in one random simulation
simulated_female_promotion_rate = simulated_female_promotions / simulation_female_n

#Calculate male promotion rate in one random simulation
simulated_male_promotion_rate = simulated_male_promotions / simulation_male_n

#Begin simulation of female promotions in 1000 simulations
simulated_female_promotion_values = [ ]

for _ in range(1000):
    simulated_female_promotion_values.append(sum(1 if random.random() < 0.5 else 0 for _ in range(simulation_female_n)))
    
simulated_female_promotion_values_np = np.array([simulated_female_promotion_values])

simulated_female_promotion_rates = simulated_female_promotion_values_np / simulation_female_n

#Begin simulation of female promotions in 1000 simulations
simulated_male_promotion_values = [ ]

for _ in range(1000):
    simulated_male_promotion_values.append(sum(1 if random.random() < 0.5 else 0 for _ in range(simulation_male_n)))
    
simulated_male_promotion_values_np = np.array([simulated_male_promotion_values])

simulated_male_promotion_rates = simulated_male_promotion_values_np / simulation_male_n

count_of_above_actual_female_promotion_rate = 0
for _ in simulated_female_promotion_rates[0]:
    if _ >= female_promotion_rate:
        count_of_above_actual_female_promotion_rate += 1

prob_of_actual_female_promotion_rate = count_of_above_actual_female_promotion_rate / len(simulated_female_promotion_rates[0])

count_of_above_actual_male_promotion_rate = 0
for _ in simulated_male_promotion_rates[0]:
    if _ >= male_promotion_rate:
        count_of_above_actual_male_promotion_rate += 1
        
prob_of_actual_male_promotion_rate = count_of_above_actual_female_promotion_rate / len(simulated_female_promotion_rates[0])