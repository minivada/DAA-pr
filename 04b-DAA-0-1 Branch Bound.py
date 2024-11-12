from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight):
        self.level = level      # Level of the node in the decision tree (or index in arr[])
        self.profit = profit    # Profit of nodes on the path from root to this node (including this node)
        self.weight = weight    # Total weight at the node

    def __lt__(self, other):
        return other.weight < self.weight  # Compare based on weight in descending order

def bound(u, n, W, arr):
    # Calculate the upper bound of profit for a node in the search tree
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    # Greedily add items to the knapsack until the weight limit is reached
    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    # If there are still items left, calculate the fractional contribution of the next item
    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):
    # Sort items based on value-to-weight ratio in non-ascending order
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0)  # Dummy node at the starting
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0)  # Starting node
        elif u.level == n - 1:
            continue  # Skip if it is the last level (no more items to consider)
        else:
            v = Node(u.level + 1, u.profit, u.weight)  # Node without considering the next item

        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value

        # If the cumulated weight is less than or equal to W and profit is greater than previous profit, update maxProfit
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v_bound = bound(v, n, W, arr)
        # If the bound value is greater than current maxProfit, add the node to the priority queue for further consideration
        if v_bound > max_profit:
            priority_queue.put(v)

        # Node considering the next item without adding it to the knapsack
        v = Node(u.level + 1, u.profit, u.weight)
        v_bound = bound(v, n, W, arr)
        # If the bound value is greater than current maxProfit, add the node to the priority queue for further consideration
        if v_bound > max_profit:
            priority_queue.put(v)

    return max_profit

# Driver program to test the above function
W = 10
arr = [
    Item(2, 40),
    Item(3.14, 50),
    Item(1.98, 100),
    Item(5, 95),
    Item(3, 30)
]
n = len(arr)

max_profit = knapsack(W, arr, n)
print("Maximum possible profit =", max_profit)








































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
