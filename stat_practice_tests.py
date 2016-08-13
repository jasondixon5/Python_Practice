#! /usr/bin/env python3
# stat_practice_tests.py

import stat_practice as sp

print("Success/Failure Test Results at p=.4, n=976: {}".format(sp.check_success_failure(.4, 976)))

print("Standard Error at .4, n=976: {}".format(sp.standard_error(.4, 976)))

print("Success/Failure Test Results at p=.5, n=5: {}".format(sp.check_success_failure(.5, 5)))

print("Confidence Interval at alpha=0.05 for p=.44, n=976: {}".format(sp.confidence_interval(0.44, .95, 976)))

print("Success/Failure Test at p=.50, n=500: {}".format(sp.check_success_failure(.50, 500)))

print("Confidence Interval at alpha=0.05 for p=.52, n=500: {}".format(sp.confidence_interval(.52, .95,500)))

print("Z-Score for p=0.5 and p-hat=.52: {}".format(sp.z_score(.5, .52, 500)))

print("Tire Sample size at p=1.7%, margin=2%, alpha=10%: {}".format(sp.sample_size_calc(.90, .02, .017)))

print("Tire Sample size at p=6.2%, margin=2%, alpha=10%: {}".format(sp.sample_size_calc(.90, .02, .062)))

print("Tire Sample size at p=1.3%, margin=2%, alpha=10%: {}".format(sp.sample_size_calc(.90, .02, .013)))

print("Congress survey Sample size at p=17%, margin=4%, alpha=5%: {}".format(sp.sample_size_calc(.95, .04, .17)))

print("Congress survey Sample size at p=17%, margin=4%, alpha=20%: {}".format(sp.sample_size_calc(.80, .04, .17)))

print("Practice 3.2.2 Success-Failure Check: {},{}".format(sp.check_success_failure(.47, 771), sp.check_success_failure(.34, 732)))

print("Practice 3.2.2 SE: {}".format(sp.standard_error_two_sample(.47, 771, .34, 732)))

print("Practice 3.2.2 CI: {}".format(sp.confidence_interval_two_sample(.47, 771, .34, 732, .9)))

print("Example 3.11 Success/Failure Test: {}, {}".format(sp.check_success_failure(958/1000,1000),sp.check_success_failure(899/1000,1000)))

print("Example 3.11 Point Estimate, Pooled SE, CI at 95%: {}, {}, {}".format((958/1000)-(899/1000), sp.standard_error_two_sample(958/1000, 1000, 899/1000, 1000), sp.confidence_interval_two_sample(958/1000, 1000, 899/1000, 1000, .95)))

print("3.1.c SE: {}".format(sp.standard_error(.08, 125)))

print("3.1.c Z-Score: {}".format(sp.z_score(.08, .12, 125)))

print("3.1.d SE: {}".format(sp.standard_error(.08, 250)))

print("3.1.d Z-Score: {}".format(sp.z_score(.08, .12, 250)))

print("3.3.b SE: {}".format(sp.standard_error(.90, 30)))

print("3.3.b SE: {}".format(sp.standard_error(.90, 30*4)))

print("3.5.d sample size at p=70%, margin=4%, alpha=05%: {}".format(sp.sample_size_calc(.95, .04, .70)))

print("3.7 SE, ME: {}, {}".format(sp.standard_error(.56, 600),(sp.standard_error(.56, 600))*1.96))

print("3.9.c SE: {}".format(sp.standard_error(.87, 400)))

print("3.9.c CI: {}".format(sp.confidence_interval(.87, .95, 400)))

print("3.9.e CI: {}".format(sp.confidence_interval(.87, .99, 400)))

print("3.11.a SE: {}".format(sp.standard_error(.55, 1509)))

print("3.11.a CI: {}".format(sp.confidence_interval(.55, .95, 1509)))

print("3.13.a SE: {}".format(sp.standard_error(.52, 783)))

print("3.1.d Z-Score: {}".format(sp.z_score(.50, .52, 783)))

print("3.15.a SE: {}".format(sp.standard_error(.17, 2254)))

print("3.15.a Success/Failure Test at p=.17, n=2254: {}".format(sp.check_success_failure(.17, 2254)))

print("3.15.a Z-Score: {}".format(sp.z_score(.38, .17, 2254)))

print("3.15.c CI: {}".format(sp.confidence_interval(.17, .95, 2254)))

print("3.17.a Success/Failure Test at p=.6625, n=80: {}".format(sp.check_success_failure(.6625, 80)))

print("3.17.a SE: {}".format(sp.standard_error(.6625, 80)))

print("3.17.a Z-Score: {}".format(sp.z_score(.5, .6625, 80)))

print("3.19.a Success/Failure Test at p=.2, n=200: {}".format(sp.check_success_failure(.2, 200)))

print("3.19.a SE: {}".format(sp.standard_error(.2, 200)))

print("3.19.c CI: {}".format(sp.confidence_interval(.2, .95, 200)))

print("3.19.b sample size at p=20%, margin=2%, CL=95%: {}".format(sp.sample_size_calc(.95, .02, .20)))

print("3.21.a sample size at p=52%, margin=1%, CL=90%: {}".format(sp.sample_size_calc(.90, .01, .52)))

print("3.27.a pooled SE: {}".format(sp.standard_error_two_sample(.7, 819, .42, 783)))

print("3.27.a pooled CI: {}".format(sp.confidence_interval_two_sample(.7, 819, .42, 783, .95)))

print("3.29.a pooled SE: {}".format(sp.standard_error_two_sample(.4425, 104, .5574, 131)))

print("3.29.a pooled SE with pooled prop: {}".format(sp.standard_error_two_sample(.2842, 438, .2842, 389)))










