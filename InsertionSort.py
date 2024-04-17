import aux_functions as aux
import sort_algortithms as sortalg
from timeit import default_timer as timer

# list of sort algorithms' names
alg_names = ["Insertion Sort"]

n_experiments = 100     # number of experiments for each array size

# list of arrays' sizes (N)
N_values = list(range(1,11)) + list(range(20,260,10))
len_n_samples = len(N_values)   # number of different arrays' sizes

# it stores the mean of time execution for each N
time_samples = [0] * len_n_samples

# loop iterates over each value of N (array size)
for i in range(len_n_samples):
    elapsed_time = [0] * n_experiments    # it stores the time for sorting 
                                          # each experiment
    
    # loop iterates over each experiment
    for j in range(n_experiments):
        array = aux.create_array(N_values[i])   # it creates an random array with
                                                # N_values[i] elements
        
        start = timer()                     # start time stamp
        sortalg.insertionSort(array)        # running the sorting algorithm
        elapsed_time[j] = timer() - start   # final time stamp (elapsed time) 
  
    # mean of the time measured for ordering each experimental array
    time_samples[i] = sum(elapsed_time) / n_experiments
    print(f" -> N_VALUES: {N_values[i]}")

# plot the results (only one sort algorithm was used in this example)
aux.plot_results(N_values, time_samples, alg_names)