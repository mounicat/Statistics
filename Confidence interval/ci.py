#calculating confidence interval when sample standard deviation is known

import scipy.stats as stats
import numpy
import matplotlib.pyplot as plt
import random
import math

def confidence_interval(population,sample_size):
    std_dev_pop = round(numpy.std(population),2)
    #print numpy.mean(population)

    sample = numpy.random.choice(a=population, size=sample_size)
    sample_mean = numpy.mean(sample)

    z_critical = stats.norm.ppf(q = 0.975)  # for 95% confidence interval
    #print("z critical value")  
    #print(z_critical)

    lower_bound = sample_mean - ( z_critical * std_dev_pop / math.sqrt(sample_size))
    upper_bound = sample_mean + ( z_critical * std_dev_pop / math.sqrt(sample_size))
    
    print "The confidence interval is [", lower_bound, ",", upper_bound,"]"
    print "Difference (Range) is ", upper_bound-lower_bound, "\n"


if __name__ == "__main__":
    population = []
    for i in range(1000):
        population.append(random.randint(1, 100))
    print "\n"
    sample_size = 20
    print "For sample size ",sample_size
    confidence_interval(population,sample_size)
    sample_size = 50
    print "For sample size ",sample_size
    confidence_interval(population,sample_size)
    sample_size = 100
    print "For sample size ",sample_size
    confidence_interval(population,sample_size)
