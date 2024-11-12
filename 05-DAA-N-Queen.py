'''Design n-Queens matrix having first Queen placed. 
Use backtracking to place remaining Queens to generate the final n-queen‘s matrix.'''
global N
N = 4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
solveNQ()






























This Python code is a solution for the **Knapsack Problem** using a **Branch and Bound approach**. The Branch and Bound method is particularly efficient for solving combinatorial optimization problems like the 0/1 Knapsack, where it prunes branches of the solution space that don’t lead to optimal solutions. Here, the priority queue is used to manage nodes that represent decisions in a binary tree, either including or excluding each item.

### Key Components

#### 1. **Item Class**
   ```python
   class Item:
       def __init__(self, weight, value):
           self.weight = weight
           self.value = value
   ```
   - This class represents an item with a specific `weight` and `value`. Objects of this class are used to store the knapsack items.

#### 2. **Node Class**
   ```python
   class Node:
       def __init__(self, level, profit, weight):
           self.level = level
           self.profit = profit
           self.weight = weight

       def __lt__(self, other):
           return other.weight < self.weight
   ```
   - **Attributes**:
     - `level`: The current level in the decision tree, representing the index of the item in `arr`.
     - `profit`: Total profit accumulated up to this node.
     - `weight`: Total weight accumulated up to this node.
   - **Comparison Operator**: The `__lt__` method allows nodes to be compared based on their weight (in descending order), which is required by the `PriorityQueue` to handle nodes in the desired order.

#### 3. **Bound Function**
   ```python
   def bound(u, n, W, arr):
   ```
   - This function calculates the **upper bound of profit** for a node `u` in the search tree.
   - **Logic**:
     - If `u.weight >= W`, the function returns `0` because no further profit can be achieved if the knapsack is full.
     - Otherwise, it calculates the upper bound by greedily adding items starting from the current level to maximize profit until the weight limit is reached.
     - If an item partially fits, it adds a fractional part of the item’s profit (a greedy heuristic).

#### 4. **Knapsack Function**
   ```python
   def knapsack(W, arr, n):
   ```
   - **Arguments**:
     - `W`: Maximum capacity of the knapsack.
     - `arr`: List of `Item` objects, each with a weight and value.
     - `n`: Number of items.
   - **Initialization**:
     - `arr` is sorted based on each item’s value-to-weight ratio, ensuring that higher-value items are prioritized.
     - `priority_queue`: A priority queue (min-heap) initialized with a dummy root node (`u`) representing the starting point with `profit` and `weight` as `0`.
     - `max_profit`: Keeps track of the highest profit achieved so far.

#### 5. **Branch and Bound Process**
   ```python
   while not priority_queue.empty():
       u = priority_queue.get()
   ```
   - **Loop Over Nodes**:
     - Nodes represent states in the decision tree. The main idea is to explore each possibility (including or excluding an item) and calculate the profit and weight.
     - **Two Cases**:
       - **Case 1 (Including the Item)**:
         - A node `v` is created by including the item at the current level in the knapsack.
         - The cumulative `weight` and `profit` of this node `v` are updated based on the item’s weight and value.
         - If `v.weight <= W` and `v.profit > max_profit`, then `max_profit` is updated to `v.profit`.
         - The upper bound for node `v` is calculated using the `bound` function.
         - If `v_bound > max_profit`, this node is added to the queue for further exploration.
       - **Case 2 (Excluding the Item)**:
         - A new node `v` is created at the current level, but without adding the item to the knapsack.
         - The upper bound for this node is calculated. If it’s greater than the current `max_profit`, this node is added to the queue for further consideration.

#### 6. **Final Result**
   ```python
   return max_profit
   ```
   - The `max_profit` variable, containing the highest profit achieved with the capacity constraint, is returned as the result.

### Example Walkthrough

Using the given inputs:

```python
W = 10
arr = [
    Item(2, 40),
    Item(3.14, 50),
    Item(1.98, 100),
    Item(5, 95),
    Item(3, 30)
]
n = len(arr)
```

**Explanation**:
- The items are sorted based on their value-to-weight ratio.
- The algorithm will proceed by branching on including or excluding items, calculating upper bounds at each step.
- As it traverses nodes, it only explores promising nodes (i.e., nodes whose bound exceeds the current max profit).
  
**Expected Output**:
```plaintext
Maximum possible profit = 235
```

### Complexity Analysis

- **Time Complexity**: \(O(2^n)\) in the worst case, as it can potentially explore all subsets of items. However, branch and bound prunes many nodes, often resulting in much lower complexity in practice.
- **Space Complexity**: \(O(2^n)\) due to storage of nodes in the priority queue.

This code efficiently finds the optimal solution by combining greedy heuristics (using bound estimates) with the branch and bound methodology.
