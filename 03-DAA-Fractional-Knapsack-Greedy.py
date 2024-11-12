def fractional_knapsack(value, weight, capacity):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value, fractions
 
 
n = int(input('Enter number of items: '))
value = input('Enter the values of the {} item(s) in order: '
              .format(n)).split()
value = [int(v) for v in value]
weight = input('Enter the positive weights of the {} item(s) in order: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))
 
max_value, fractions = fractional_knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions)





































# This Python code implements the **Fractional Knapsack problem**. The objective of this problem is to maximize the total value of items in a knapsack without exceeding its weight capacity. Unlike the 0/1 Knapsack problem, the Fractional Knapsack allows us to take fractional parts of items, which is a hallmark of the greedy approach used here.

# ### Breakdown of Code Components

# #### 1. **Function Definition: `fractional_knapsack`**
#    ```python
#    def fractional_knapsack(value, weight, capacity):
#    ```
#    - This function calculates the maximum value of items that can be placed in the knapsack while adhering to the capacity constraint.
#    - It takes in three parameters:
#      - `value`: a list containing the values of each item.
#      - `weight`: a list containing the weights of each item.
#      - `capacity`: the maximum weight the knapsack can hold.

# #### 2. **Input Parameters and Index Preparation**
#    ```python
#    index = list(range(len(value)))
#    ratio = [v/w for v, w in zip(value, weight)]
#    ```
#    - `index` is a list of indices representing each item. For `n` items, this list would be `[0, 1, 2, ..., n-1]`.
#    - `ratio` calculates the value-to-weight ratio for each item using a list comprehension. Each `ratio[i]` represents how valuable each unit of weight for item `i` is, given by `value[i] / weight[i]`.

# #### 3. **Sorting Items by Value-to-Weight Ratio**
#    ```python
#    index.sort(key=lambda i: ratio[i], reverse=True)
#    ```
#    - The items are sorted based on their value-to-weight ratio in descending order. This sorting ensures that we prioritize items with the highest value per unit weight first, maximizing the knapsack’s value while minimizing its weight.
#    - Sorting is done by reordering the `index` list based on the `ratio` list. Higher ratios are placed at the beginning of `index`, indicating a greedy approach.

# #### 4. **Main Loop to Compute Maximum Value and Fractions**
#    ```python
#    max_value = 0
#    fractions = [0]*len(value)
#    for i in index:
#    ```
#    - `max_value`: initializes to zero, representing the total value of items that can be placed in the knapsack.
#    - `fractions`: a list initialized with zeros, where each `fractions[i]` will represent the fraction of item `i` taken. For example, `1` means the entire item is taken, `0.5` means half, and `0` means none of that item is taken.

#    The loop iterates through each item in the sorted `index` list:

#    ```python
#        if weight[i] <= capacity:
#            fractions[i] = 1
#            max_value += value[i]
#            capacity -= weight[i]
#    ```
#    - If the weight of the current item `i` is less than or equal to the remaining capacity of the knapsack, the entire item is taken.
#    - `fractions[i]` is set to `1`, representing the full inclusion of item `i`.
#    - `max_value` is updated by adding the value of item `i`.
#    - `capacity` is reduced by the weight of item `i` because it is now included in the knapsack.

#    ```python
#        else:
#            fractions[i] = capacity / weight[i]
#            max_value += value[i] * capacity / weight[i]
#            break
#    ```
#    - If the item’s weight exceeds the remaining capacity, only a fraction of it can be taken. `fractions[i]` is set to the fraction that fits in the remaining capacity.
#    - `max_value` is updated by adding the proportional value of this fraction.
#    - The loop is broken since the knapsack is now filled to its capacity.

#    Once the loop completes, the function returns `max_value` and `fractions`.

# #### 5. **Taking User Input and Displaying Results**
#    ```python
#    n = int(input('Enter number of items: '))
#    value = input('Enter the values of the {} item(s) in order: '.format(n)).split()
#    value = [int(v) for v in value]
#    weight = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split()
#    weight = [int(w) for w in weight]
#    capacity = int(input('Enter maximum weight: '))
#    ```
#    - Here, the user is prompted to enter the number of items (`n`), values, weights, and the knapsack's maximum capacity.
#    - The values and weights are input as space-separated strings, which are then split and converted to lists of integers.

#    ```python
#    max_value, fractions = fractional_knapsack(value, weight, capacity)
#    ```
#    - `fractional_knapsack` is called with these inputs, returning `max_value` and `fractions`.

#    ```python
#    print('The maximum value of items that can be carried:', max_value)
#    print('The fractions in which the items should be taken:', fractions)
#    ```
#    - Finally, the code displays the maximum value that can be achieved within the capacity and the fraction of each item taken.

# ### Example Walkthrough
# Let’s say:
# - `value = [60, 100, 120]`
# - `weight = [10, 20, 30]`
# - `capacity = 50`

# 1. The value-to-weight ratios are calculated as `[6, 5, 4]`.
# 2. Items are sorted by these ratios: item 0 (60), item 1 (100), and item 2 (120).
# 3. The algorithm begins filling the knapsack:
#    - Item 0 is fully included (`fractions[0] = 1`), adding 60 to `max_value` and reducing `capacity` by 10.
#    - Item 1 is also fully included (`fractions[1] = 1`), adding 100 to `max_value` and reducing `capacity` by 20.
#    - For item 2, only a fraction (20/30) can be included, so `fractions[2] = 0.67` and `max_value` is updated accordingly.

# The code thus outputs the maximum value of items that can be carried and the fractions of each item taken to achieve that value.

