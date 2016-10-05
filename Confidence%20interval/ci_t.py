#calculating confidence interval when population standard deviation is not known

import scipy.stats as stats
import numpy
import matplotlib.pyplot as plt
import random
import math

def confidence_interval(sample_size):
    population = []
    for i in range(1000):
        population.append(random.randint(1, 100))

    sample = numpy.random.choice(a=population, size=sample_size)
    sample_mean = numpy.mean(sample)

    t_critical = stats.t.ppf(q = 0.975,df=(sample_size-1))  # for 95% confidence interval
    #print("t critical value")  
    #print(t_critical)
    std_dev_sample = sample.std()
    lower_bound = sample_mean - ( t_critical * std_dev_sample / math.sqrt(sample_size))
    upper_bound = sample_mean + ( t_critical * std_dev_sample / math.sqrt(sample_size))
    
    print "The confidence interval is (", lower_bound, ",", upper_bound,")"
    print "Difference (Range) is ", upper_bound-lower_bound, "\n"


if __name__ == "__main__":
 
    print "\n"
    sample_size = 20
    print "For sample size ",sample_size
    confidence_interval(sample_size)
    sample_size = 50
    print "For sample size ",sample_size
    confidence_interval(sample_size)
    sample_size = 100
    print "For sample size ",sample_size
    confidence_interval(sample_size)

