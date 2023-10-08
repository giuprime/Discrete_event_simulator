import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

# Declaration of the class
class Simulation:
    def __init__(self):
        # Declaration of the global variable

        # Number of costumer in the system for convention we start from 0
        self.num_in_system = 0
        self.clock = 0.0
        # Arrival time
        self.t_arrival = self.generate_interarrival()
        # Time opf depart equal to infinity
        self.t_depart = float('inf')

        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def advance_time(self):

        t_events = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_in_system*(t_events - self.clock)
        # Update of the clock
        self.clock = t_events
        # If the arrival event arrive first
        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
        # Departure time before the arrival
        else:
            self.handle_depart_event()

    def handle_arrival_event(self):
        # Increment the number of costumer
        self.num_in_system += 1
        # Increment the number of the arrivals
        self.num_arrivals += 1

        #I consider if the costumer that arrive is the only one in the system
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    # Function for the handle of the departure
    def handle_depart_event(self):
        # Decrement the costumer in the system
        self.num_in_system -= 1
        # Increment the number of departure
        self.num_departs += 1
        # Condition for the last departure
        if self.num_in_system >= 0:
            self.t_depart = self.clock + self.generate_service()
        else:
            # No costumer in the system
            self.t_depart = float('inf')
    # Generation of the interarrival
    def generate_interarrival(self):
        # Use the random generator and the exponential distribution
        return np.random.exponential(1./3)
    #passare i parametri da input
    # Function for the generation of the service in a random way
    def generate_service(self):
        # Use also the random generator and the exponential, but the average is 4 costumer per minute
        return np.random.exponential(1./4)


np.random.seed(0)

s = Simulation()
for i in range (100):
    print(s.advance_time())

    print("Generate interarrival, lambda: ", round(s.generate_interarrival(), 3))
    print("Generate service, mu ",round(s.generate_service(), 3))

    print("Probability is equalt to: ", round( (s.generate_interarrival() / s.generate_service()), 3 ))

    p0 = (1-(s.generate_interarrival() / s.generate_service()))
    print("Probability P0: ", round(p0, 3))

    print("Probability that the server is busy is: ", round(1-(p0), 3))

    average_costumer_number = (s.generate_interarrival() / s.generate_service() - s.generate_interarrival() )
    print("The average number of costumer in the system is: ", round(average_costumer_number, 3), "hours")

    average_time = average_costumer_number / s.generate_interarrival()
    print("The average time in the system is: ", round(average_time, 3), "hours")

    n = pow(s.generate_interarrival(), 2) / s.generate_service()*(s.generate_service() - s.generate_interarrival())
    print("The number of customer in the queue is ", round(n, 3))

    print("System clock: ", round(s.clock, 3))
    print("Costumer in the system: ", round(s.num_in_system, 3))
    print("Time arrival: ", round(s.t_arrival, 3))
    print("Time departure: ", round(s.t_depart, 3))
    print("Total wait: ", round(s.total_wait, 3))
    print("Number of departure: ", round(s.num_departs, 3))
    print("-----------------------------------------------------")

print("Average time wait in the system for customer: ", s.total_wait / s.num_departs)

"""_lambda = 1./3
_lambda1 = 1./4

plot_x = np.linspace(0,100) #linspace: generate a linear space and the range is in the round bracket
pdf_interarrival = 1/s.total_wait*math.exp(-1/s.total_wait)
#print("PDF interarrival: ",pdf_interarrival)

cdf_interarrival = 1-np.exp(-_lambda*plot_x)
print("The CDF for the interarrival is equal to: ",cdf_interarrival)


cdf_service = 1-np.exp(-_lambda1*plot_x)
print("The CDF for the service is equal to: ", cdf_service)

plt.figure("Figura 1")
plt.plot(plot_x, stats.expon.pdf(plot_x, scale = 1./_lambda) * 100)
plt.plot(plot_x, stats.expon.pdf(plot_x, scale = 1./_lambda1) * 100)
plt.show()

plt.figure("Figura PDF function arrival")
#plt.plot(plot_x,pdf_interarrival)
plt.plot(plot_x, stats.expon.pdf(plot_x, scale = 1./_lambda), '--r')
plt.xlabel("Inter-arrival Time x (minute)")
plt.ylabel("f(x)")
plt.show()

plt.figure("Figura PDF function service")
plt.plot(plot_x, stats.expon.pdf(plot_x, scale = 1./_lambda1), '--b')
plt.xlabel("Service Time x (minute)")
plt.ylabel("f(x)")
plt.show()

plt.figure("Figura CDF function interarrival")
plt.plot(plot_x, cdf_interarrival)
plt.plot(plot_x, stats.expon.cdf(plot_x, scale = 1./_lambda), "--r")
plt.xlabel("Inter-arrival Time x (minute)")
plt.ylabel("f(x)")
plt.show()

plt.figure("Figura CDF function service")
plt.plot(plot_x, cdf_service)
plt.plot(plot_x, stats.expon.cdf(plot_x, scale = 1./_lambda1), "--b")
plt.xlabel("Service Time x (minute)")
plt.ylabel("f(x)")
plt.show()"""
#0.19680028807931768
#0.18368283036516642