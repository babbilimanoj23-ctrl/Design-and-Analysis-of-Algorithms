import time

# Function for Iterative Factorial
# Time Complexity: O(n)
# Space Complexity: O(1)
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Function for Recursive Factorial
# Time Complexity: O(n)
# Space Complexity: O(n) due to call stack
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# Main Program
try:
    n = int(input("Enter a non-negative integer (e.g., 20): "))

    if n < 0:
        print("Invalid input! Please enter a non-negative integer.")
    else:

        # Measure Iterative Implementation
        start_iter = time.perf_counter_ns()
        res_iter = factorial_iterative(n)
        end_iter = time.perf_counter_ns()

        duration_iter = end_iter - start_iter

        # Measure Recursive Implementation
        start_rec = time.perf_counter_ns()
        res_rec = factorial_recursive(n)
        end_rec = time.perf_counter_ns()

        duration_rec = end_rec - start_rec

        # Output Results
        print(f"\n--- Results for {n}! ---")
        print("Iterative Result :", res_iter)
        print("Iterative Time   :", duration_iter, "ns")
        print("-------------------------------")
        print("Recursive Result :", res_rec)
        print("Recursive Time   :", duration_rec, "ns")

except ValueError:
    print("Invalid input! Please enter a non-negative integer.")