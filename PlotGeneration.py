'''
This script generates plots for the paper
"A note on the uniqueness of Nash–Cournot equilibria in 
an oligopolistic energy market with renewable generation 
and demand uncertainty", Energy Economics, October 2024
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.integrate import quad

'''
Set up functions for calculating distributions and best response:
'''

expectedValFunc = lambda x: x*(d1*dist1.pdf(x) + d2*dist2.pdf(x))


def CDF(l):
    return((d1*dist1.cdf(l) + d2*dist2.cdf(l)) )


def PDF(x):
    return( d1*dist1.pdf(x)  + d2*dist2.pdf(x) )
  
    
def PrintParams(distribution):
    print(f"alpha_star: {alpha_star}")
    print(f"Renewable: {R}")
    print(f"firms: {numberOfFirms}")
    print(f"cost slope: {cost_slope:.3f}")
    print(f"price slope: {price_slope:.3f}")
    print(f"Distribution: {distribution}")


def Response(Q):

    upperLim = alpha_star
    lowerLim = price_slope*(Q + R)

    num = quad(expectedValFunc,lowerLim,upperLim, limit = 200)[0] - cost_slope
    denom = price_slope*(1.0 - CDF(lowerLim))

    t1 = num/denom
    t2 = Q + (1.0 + delta/numberOfFirms)*R
    return(t1 - t2)


def PlotResponse(name = '', display = False):
    
    figure = plt.figure()


    x = np.linspace(0, (alpha_star/price_slope) - R - 100, 100) 

    z = [Response(g) for g in x]

    qn = [i/numberOfFirms for i in x]

    plt.plot(x,z, 'k',label = "Inclusive Best Response Function")
    plt.plot(x,qn, 'k--',label = "Q/n")

    plt.plot([0,(alpha_star/price_slope) - R - 100],[0,0],'k:')
    plt.legend()
    plt.xlabel("Total Quantity (MWh)")
    plt.ylabel("Quantity per Firm (MWh)")
    if name != '':
        plt.savefig(name, bbox_inches = 'tight', pad_inches =0.1, dpi = 200)
    
    if display:
		plt.show()
		
        
'''
Graphical representation of symmetric equilibria:
'''        

figure = plt.figure()
x = np.linspace(0, (alpha_star/price_slope) - R - 100, 100) 

numberOfFirms = 3.0
qn = [i/numberOfFirms for i in x]
plt.plot(x,qn, 'k--',label = "Q/n")
plt.legend()
plt.xlabel("Total Quantity (MWh)")
plt.ylabel("Firm i Production (MWh)")
plt.grid()
plt.savefig("qnLine", bbox_inches = 'tight', pad_inches =0.1, dpi = 200)



'''
Demand following uniform distribution:
'''
# unique equilibrium
numberOfFirms = 3.0
delta = 1.0
R = 100
alpha_star = 750
price_slope = 1.3
cost_slope = 2.4

dist1 = stats.norm(700,20)
d1 = 0.0
dist2 = stats.uniform(0,750)
d2 = 1-d1
a
PrintParams("Uniform 0-750")
PlotResponse("UniformUnique.jpg")

# no profitable equilibrium
numberOfFirms = 3.0
delta = 1.0
R = 375
alpha_star = 750
price_slope = 1.3
cost_slope = 2.4

dist1 = stats.norm(700,20)
d1 = 0.0
dist2 = stats.uniform(0,750)
d2 = 1-d1

PrintParams("Uniform 0-750")
PlotResponse("UniformNoEq.jpg")


'''
demand following bimodal distribution
'''
# multiple equilibria
numberOfFirms = 3.0
delta = 1.0
R = 100
alpha_star = 750
price_slope = 1.3
cost_slope = 2.4

dist1 = stats.triang(0.5,650,100) 
d1 = 0.25
dist2 = stats.triang(0.5,350,150)
d2 = 1-d1

PrintParams("Mixture - 25% T(700,10), 75% N(400,20)")
PlotResponse("BiModalMultipleEq.jpg")

#unique equilibrium

numberOfFirms = 3.0
delta = 1.0
R = 380
alpha_star = 750
price_slope = 1.3
cost_slope = 2.4

dist1 = stats.triang(0.5,650,100)  
d1 = 0.3
dist2 = stats.triang(0.5,350,150)
d2 = 1-d1

PrintParams("Mixture - 30% N(700,10), 70% N(400,20)")
PlotResponse("BiModalUniqueEq.jpg")

#unique equilibrium, assumption 2 violated

numberOfFirms = 3.0
delta = 1.0
R = 350
alpha_star = 750
price_slope = 1.3
cost_slope = 2.4

dist1 = stats.triang(0.5,650,100) 
d1 = 0.3
dist2 = stats.triang(0.5,350,150)
d2 = 1-d1

PrintParams("Mixture - 30% N(700,10), 70% N(400,20)")
PlotResponse('BiModalUniqueEq_Assumption2Violated')

        
        

    
    plt.show()
