import aux_functions as aux
import sort_algortithms as sortalg
from timeit import default_timer as timer

# List of sort algorithms' names
alg_names = ["Merge Sort", "Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort"]

n_experiments = 100  # Number of experiments for each array size

# List of arrays' sizes (N)
N_values = list(range(1, 11)) + list(range(20, 1000, 10))
len_n_samples = len(N_values)  # Number of different arrays' sizes

# It stores the mean of time execution for each N and each algorithm
time_samples = [[0] * len_n_samples for _ in range(len(alg_names))]

# Loop iterates over each value of N (array size)
for i in range(len_n_samples):
    # Loop iterates over each algorithm
    for alg_index, alg_name in enumerate(alg_names):
        elapsed_time = [0] * n_experiments  # It stores the time for sorting each experiment

        # Loop iterates over each experiment
        for j in range(n_experiments):
            array = aux.create_array(N_values[i])  # It creates a random array with N_values[i] elements

            start = timer()  # Start time stamp
            if alg_name == "Merge Sort": #codigo implementado
                sortalg.merge_sort(array)
            elif alg_name == "Bubble Sort":
                sortalg.bubbleSort(array)
            elif alg_name == "Insertion Sort":
                sortalg.insertionSort(array)
            elif alg_name == "Quick Sort":
                sortalg.quicksort(array)
            elif alg_name == "Selection Sort":
                sortalg.selectionSort(array)
            elapsed_time[j] = timer() - start  # Final time stamp (elapsed time)

        # Mean of the time measured for ordering each experimental array
        time_samples[alg_index][i] = sum(elapsed_time) / n_experiments
        print(f" -> Algorithm: {alg_name}, N_VALUES: {N_values[i]}")

# Plot the results for all algorithms
aux.plot_results(N_values, time_samples, alg_names)
