#! /usr/bin/env python3
# ANOVA_compare.py
# A test script to compare the ANOVA_practice and ANOVA_practice2 scripts for accuracy/results


low_cal = [8, 9, 6, 7, 3]
low_fat = [2, 4, 3, 5, 1]
low_carb = [3, 5, 4, 2, 3]
control = [2, 2, -1, 0, 3]

import ANOVA_practice as a
import ANOVA_practice2 as a2

ssb_result = a.ssb(low_cal, low_fat, low_carb, control)
ssb_result2 = a2.ssb(low_cal, low_fat, low_carb, control)
assert ssb_result == ssb_result2, "Pass"

sse_result = a.sse(low_cal, low_fat, low_carb, control)
sse_result2 = a2.sse(low_cal, low_fat, low_carb, control)
assert ssb_result == ssb_result2, "Pass"

f_result = a.fStatistic(low_cal, low_fat, low_carb, control)
f_result2 = a2.fStatistic(low_cal, low_fat, low_carb, control)
assert ssb_result == ssb_result2, "Pass"

print(ssb_result)
print(ssb_result2)
print(sse_result)
print(sse_result2)
print(f_result)
print(f_result2)
