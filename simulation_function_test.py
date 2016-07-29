#! /usr/bin/env python3

import simulation_functions as sf

male_observed = [21, 3]
female_observed = [14, 10]
all_results = [male_observed, female_observed]

m2f_diff_results = sf.diff_proportion(all_results)

print(m2f_diff_results)