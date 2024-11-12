import random
import time

def quick_sort_deterministic(arr, low, high):
    if low < high:
        pi = partition_deterministic(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)

def partition_deterministic(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = partition_randomized(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)

def partition_randomized(arr, low, high):
    pivot_index = random.randint(low, high)  # Choosing a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def analyze_quick_sort(arr):
    def measure_time(sort_func, arr):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        return end_time - start_time

    print("Array size:", len(arr))

    deterministic_time = measure_time(quick_sort_deterministic, arr)
    print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")

    randomized_time = measure_time(quick_sort_randomized, arr)
    print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")

if __name__ == "__main__":
    # Test cases with different array sizes
    sizes = [100, 1000, 5000]

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print("\nTesting with array of size", size)
        analyze_quick_sort(arr)













































This code implements and compares two versions of the **Quick Sort algorithm**: **Deterministic Quick Sort** and **Randomized Quick Sort**. It also includes functionality to analyze their performance in terms of execution time on different input array sizes.

### Explanation of Key Components

#### 1. **Deterministic Quick Sort** (`quick_sort_deterministic`)
   ```python
   def quick_sort_deterministic(arr, low, high):
       if low < high:
           pi = partition_deterministic(arr, low, high)
           quick_sort_deterministic(arr, low, pi - 1)
           quick_sort_deterministic(arr, pi + 1, high)
   ```
   - This function performs Quick Sort by selecting the **last element** in the range as the pivot. 
   - It uses the `partition_deterministic` function to partition the array based on this fixed pivot.
   - After partitioning, it recursively sorts the two subarrays (`low` to `pi-1` and `pi+1` to `high`).

#### 2. **Deterministic Partitioning** (`partition_deterministic`)
   ```python
   def partition_deterministic(arr, low, high):
       pivot = arr[high]  # Choosing the last element as the pivot
       i = low - 1
       for j in range(low, high):
           if arr[j] <= pivot:
               i += 1
               arr[i], arr[j] = arr[j], arr[i]
       arr[i + 1], arr[high] = arr[high], arr[i + 1]
       return i + 1
   ```
   - **Pivot Selection**: The last element of the current range is chosen as the pivot.
   - **Partitioning**:
     - Elements less than or equal to the pivot are moved to the left of the pivot.
     - Elements greater than the pivot remain on the right.
   - **Return Value**: It returns the final index (`i+1`) where the pivot is placed, which divides the array into two parts.

#### 3. **Randomized Quick Sort** (`quick_sort_randomized`)
   ```python
   def quick_sort_randomized(arr, low, high):
       if low < high:
           pi = partition_randomized(arr, low, high)
           quick_sort_randomized(arr, low, pi - 1)
           quick_sort_randomized(arr, pi + 1, high)
   ```
   - This version uses a **randomly selected pivot** element for partitioning.
   - It calls `partition_randomized` to partition the array.

#### 4. **Randomized Partitioning** (`partition_randomized`)
   ```python
   def partition_randomized(arr, low, high):
       pivot_index = random.randint(low, high)  # Choosing a random pivot
       arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
       pivot = arr[high]
       i = low - 1
       for j in range(low, high):
           if arr[j] <= pivot:
               i += 1
               arr[i], arr[j] = arr[j], arr[i]
       arr[i + 1], arr[high] = arr[high], arr[i + 1]
       return i + 1
   ```
   - **Random Pivot Selection**: A random index within the range is chosen as the pivot.
   - **Partitioning Process**: Similar to the deterministic partitioning, with elements moved based on their comparison to the pivot.
   - **Randomized Advantage**: Choosing a random pivot reduces the likelihood of worst-case performance on already sorted or nearly sorted arrays.

#### 5. **Performance Analysis Function** (`analyze_quick_sort`)
   ```python
   def analyze_quick_sort(arr):
       def measure_time(sort_func, arr):
           arr_copy = arr.copy()
           start_time = time.time()
           sort_func(arr_copy, 0, len(arr_copy) - 1)
           end_time = time.time()
           return end_time - start_time

       print("Array size:", len(arr))

       deterministic_time = measure_time(quick_sort_deterministic, arr)
       print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")

       randomized_time = measure_time(quick_sort_randomized, arr)
       print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")
   ```
   - **Purpose**: This function compares the execution times of both Quick Sort versions on the same array.
   - **measure_time**: Helper function that:
     - Creates a copy of the array (to avoid in-place sorting that would affect the next sort).
     - Measures the time taken to sort it using a specified sort function.
   - **Output**: It prints the time taken for both Deterministic and Randomized Quick Sorts on each array size.

#### 6. **Main Execution Block**
   ```python
   if __name__ == "__main__":
       sizes = [100, 1000, 5000]

       for size in sizes:
           arr = [random.randint(0, 10000) for _ in range(size)]
           print("\nTesting with array of size", size)
           analyze_quick_sort(arr)
   ```
   - **Array Generation**: Creates random arrays of various sizes to test the Quick Sort implementations.
   - **Function Call**: Calls `analyze_quick_sort` for each array size and prints the time results for each sort type.

### Expected Output
The code will output the execution times for Deterministic and Randomized Quick Sort on arrays of different sizes.

### Complexity Analysis
- **Time Complexity**:
  - **Deterministic Quick Sort**: \(O(n^2)\) in the worst case if the pivot is poorly chosen (e.g., already sorted array).
  - **Randomized Quick Sort**: Averages \(O(n \log n)\) by reducing the chance of hitting the worst case.
- **Space Complexity**: Both versions use \(O(\log n)\) additional space on average for recursive calls.

### Summary
- The **Deterministic version** always picks the last element as the pivot, making it sensitive to certain inputs.
- The **Randomized version** picks a random pivot, enhancing performance by reducing the chance of worst-case behavior.
- The `analyze_quick_sort` function allows you to observe time differences, illustrating the benefit of randomization in Quick Sort.


