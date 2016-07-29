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

    return (proportion_difference, r_cat1_n, r_cat2_n, proportion_R1C1, proportion_R2C1)

