import random
import numpy
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
#import plotly.plotly as py
population = []


for i in range(1000):
    population.append(random.randint(1, 100))
#print population
#print population[998]
plt.hist(population)
plt.title("Population histogram")
plt.xlabel('Age')
plt.ylabel("Frequency")
plt.show()
print "Mean"
print round(numpy.mean(population),2)
print "---------------------------------------------------------------------------"
print "Std dev"
print round(numpy.std(population),2)
std_pop = round(numpy.std(population),2)
print "---------------------------------------------------------------------------"

print "Taking 4000 random samples of size 25 each"
sample_means = []
for i in range(4000):
    samp_pop = numpy.random.choice(a=population, size=25)
    sample_means.append(numpy.mean(samp_pop))#list of means    

mu, std = norm.fit(sample_means)
plt.hist(sample_means, bins=4000, normed=True)
xmin, xmax = plt.xlim()
x = numpy.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Sampling distribution: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.show()
print "Mean of the sampling distribution"
print round(mu,2)
print "Mean of the sampling distribution is nearly equal to the population mean!"
print "---------------------------------------------------------------------------"
print "Standard error"
print round(std,2)
print "Standard error is nearly equal to ", round(numpy.std(population),2),"/", 5
print "---------------------------------------------------------------------------"       



    
