def knapSack(W, wt, val): 
    n=len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1]  
+ table[i-1][j-wt[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 
 
val = [50,100,150,200]
wt = [8,16,32,40]
W = 64
 
print(knapSack(W, wt, val))































This Python code is a solution for the **0/1 Knapsack problem** using dynamic programming. In this problem, given a set of items, each with a weight and a value, the goal is to determine the maximum value that can be obtained by selecting items with a total weight not exceeding a given capacity. The "0/1" aspect means that each item can either be included entirely in the knapsack or not included at all — no fractional items are allowed.

### Explanation of Code Components

#### 1. **Function Definition: `knapSack(W, wt, val)`**
   ```python
   def knapSack(W, wt, val):
   ```
   - This function takes three parameters:
     - `W`: the maximum capacity of the knapsack.
     - `wt`: a list of weights for each item.
     - `val`: a list of values for each item.
   - It returns the maximum value achievable within the weight capacity `W`.

#### 2. **Initialize Variables**
   ```python
   n = len(val)
   table = [[0 for x in range(W + 1)] for x in range(n + 1)]
   ```
   - `n` represents the number of items.
   - `table`: a 2D list (table) of dimensions `(n+1) x (W+1)` initialized with zeros. `table[i][j]` will store the maximum value achievable with the first `i` items and a knapsack capacity of `j`.
     - The extra row and column (for `n+1` items and `W+1` capacities) handle the base cases (e.g., no items or zero capacity).
  
#### 3. **Filling the DP Table**
   ```python
   for i in range(n + 1): 
       for j in range(W + 1): 
   ```
   - A nested loop is used to fill the table. The outer loop iterates through items (`i` from `0` to `n`), and the inner loop iterates through possible capacities (`j` from `0` to `W`).

   ##### Base Case
   ```python
   if i == 0 or j == 0:
       table[i][j] = 0
   ```
   - If `i == 0` (no items) or `j == 0` (zero capacity), `table[i][j]` is set to `0`. This makes sense because if we have no items or no capacity, the maximum value achievable is `0`.

   ##### Decision to Include or Exclude an Item
   ```python
   elif wt[i-1] <= j:
       table[i][j] = max(val[i-1] + table[i-1][j - wt[i-1]], table[i-1][j])
   ```
   - If the weight of the current item `wt[i-1]` is less than or equal to the current capacity `j`, we have a choice:
     - **Include the item**: In this case, we add the item’s value `val[i-1]` to the value obtained by filling the knapsack with the remaining capacity `j - wt[i-1]` using previous items (`table[i-1][j - wt[i-1]]`).
     - **Exclude the item**: In this case, the maximum value is simply the value obtainable without this item, given by `table[i-1][j]`.
   - We take the maximum of these two choices to ensure that we get the highest possible value for `table[i][j]`.

   ```python
   else:
       table[i][j] = table[i-1][j]
   ```
   - If the current item’s weight exceeds the current capacity (`wt[i-1] > j`), we cannot include this item. Therefore, the maximum value is simply the value obtained by excluding the item, i.e., `table[i-1][j]`.

#### 4. **Result**
   ```python
   return table[n][W]
   ```
   - After the loops complete, `table[n][W]` contains the maximum value achievable with `n` items and a knapsack capacity of `W`, which is the result returned by the function.

### Example Walkthrough

Let’s go through a small example with the provided values and weights to understand the table filling process.

```python
val = [50, 100, 150, 200]
wt = [8, 16, 32, 40]
W = 64
```

1. **Initialization**: 
   - The `table` has dimensions `5 x 65` (for 4 items and capacities from 0 to 64).
   - Initially, all cells are set to zero.

2. **Filling the DP Table**:
   - For `i=1` and `j=0` to `64`, we evaluate each item's inclusion based on capacity:
     - At `j=8`, the first item (value 50, weight 8) can be included. We update `table[1][8]` to `50` (since including this item gives a maximum value of `50`).
     - As we continue, the table will be filled considering the choices of including or excluding items.

3. **Final Result**:
   - The value in `table[4][64]` will represent the maximum value achievable with the given items and knapsack capacity.

### Output

The code will output:

```plaintext
The maximum value that can be carried: 350
```

### Complexity Analysis
- **Time Complexity**: \(O(n \times W)\), as it involves a nested loop over `n` items and `W` capacity values.
- **Space Complexity**: \(O(n \times W)\) due to the 2D `table`.

This is an efficient solution for the 0/1 Knapsack problem where we need exact solutions within the capacity constraint.
