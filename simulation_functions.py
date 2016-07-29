#! /usr/bin/env python3

import random
import numpy as np

def diff_proportion(observations, cat1_column=0, cat2_column=1):
    """
    Calculate difference in proportions
    
    cat1_column = # of first column to calculate proportion
    (0-indexed, defaults to first column)
    cat2_column = # of second column to calculate proportion
    (0-indexed, defaults to second column)
    
    observations = each row's list of values for each column
    observations represent how many values were observed for each column category

    Example: 2x2 table with following format:

    row_category    column_category
                    c_cat1          c_cat2
    r_cat1          R1C1            R1C2
    r_cat2          R2C1            R2C2

    r_cat1_observations = [R1C1, R1C2...]
    r_cat2_observations = [R2C1, R2C2...]
    observations = [r_cat1_observations, r_cat_2_observations]
    """
    c_cat1_idx = cat1_column
    c_cat2_idx = cat2_column
    r_cat1_idx = 0
    r_cat2_idx = 1
    
    #Calculate sample size (n) for each row category
    r_cat1_n = sum(observations[0])
    r_cat2_n = sum(observations[1])
    
    proportion_R1C1 = observations[r_cat1_idx][c_cat1_idx] / r_cat1_n
    proportion_R2C1 = observations[r_cat2_idx][c_cat1_idx] / r_cat2_n
    
    proportion_difference = proportion_R1C1 - proportion_R2C1
    
    #Form list of just observed values in column category 1
    c_cat1_obs = []

    for i in range(len(observations)):
        c_cat1_obs.append(observations[i][c_cat1_idx])
    
    simulated_cat1_n = sum(c_cat1_obs)
    
    large_sim_diff_rate_R1toR2 = []
    
    sim_size = 10000
    
    for _ in range(sim_size):
        simulated_results_C1R1 = 0
        simulated_results_C1R2 = 0
    
        for _ in range(simulated_cat1_n):
            if random.random() < 0.5:
                simulated_results_C1R2 += 1
            else:
                simulated_results_C1R1 += 1
        
        simulated_rate_R2C1 = simulated_results_C1R2 / simulated_cat1_n
    
        simulated_rate_R1C1 = simulated_results_C1R1 / simulated_cat1_n
    
        diff_in_simulated_rate_R1toR2 = simulated_rate_R1C1 - simulated_rate_R2C1
        
        large_sim_diff_rate_R1toR2.append(diff_in_simulated_rate_R1toR2)

    count_diffs_as_large = 0
    
    for i in large_sim_diff_rate_R1toR2:
        if i >= proportion_difference:
            count_diffs_as_large += 1
    
    p_value_proportion_difference = count_diffs_as_large / sim_size
    
    return ("""
    proportion difference: {}, 
    proportion R1C1: {}, 
    proportion R2C1: {}, 
    p-value: {}
    sim_size: {}""".format(proportion_difference, proportion_R1C1, proportion_R2C1, p_value_proportion_difference, sim_size))
    

