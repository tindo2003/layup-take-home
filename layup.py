import time
import matplotlib.pyplot as plt
def calculate_sequence_value(n: int) -> int:
    """
    Calculates the value of the sequence S(n) based on the given recurrence relation.

    Args:
        n (int): The index of the sequence value to calculate.

    Returns:
        int: The calculated value of S(n).
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    sequence_values = [1, 2]

    for i in range(3, n + 1):
        if i % 2 == 0:  
            next_value = sequence_values[1] + sequence_values[0]
        else: 
            next_value = 2 * sequence_values[1] - sequence_values[0]

        sequence_values[0] = sequence_values[1]
        sequence_values[1] = next_value

    return sequence_values[1]

if __name__ == "__main__":
	n = 10000
	start_time = time.time()
	result = calculate_sequence_value(n)
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"S({n}) = {result}")
	print(f"Execution time: {execution_time: .6f} seconds")
	
	n_values = range(100, 10001, 100)  # Test values from 100 to 10000
	runtimes = []

	# Measure runtime for each n
	for n in n_values:
		start_time = time.time()
		calculate_sequence_value(n)
		end_time = time.time()
		runtime = end_time - start_time
		runtimes.append(runtime)

	# Create the plot
	plt.plot(n_values, runtimes)  # Removed marker for a smoother line
	plt.xlabel('n')
	plt.ylabel('Runtime (seconds)')
	plt.title('Runtime vs. n for Sequence Calculation')
	plt.grid(True)
	plt.show()
