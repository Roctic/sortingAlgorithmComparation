import random
import matplotlib.pyplot as plt

# Create an array of n random elements
# n_elements: size of the array (number of elements)
def create_array(n_elements):
    return random.sample(range(1,(n_elements+1) * 10), n_elements)

# Plot the Sort Algorithms Comparison graph
# N_values: array sizes list
# time_elapsed: mean of time elapsed for each array size N
# alg_names: algorithms' name list
def plot_results(N_values, time_elapsed, alg_names):
    for i, alg_name in enumerate(alg_names): #codigo implementado
        plt.plot(N_values, time_elapsed[i], label=alg_name, lw=2)
    
    plt.grid()      # show grid
    plt.title("Sort Algorithms Comparison")     # defining the title
    plt.legend(loc="upper left")                # positioning the legend
    plt.xlabel("N")                             # x axis label
    plt.ylabel("time elapsed in seconds")       # y axis label
    plt.show()                                  # show the graph