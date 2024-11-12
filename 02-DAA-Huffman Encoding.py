# Huffman Coding in python

string = 'BCAADDDCCACACAC'

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
































This code implements **Huffman Coding**, an algorithm for lossless data compression. Here's a breakdown of the code's workflow:

### 1. **Understanding the String and Frequency Calculation**
   ```python
   string = 'BCAADDDCCACACAC'
   ```
   This is the input string that we want to compress using Huffman coding. The algorithm works by assigning shorter binary codes to frequently occurring characters and longer codes to less frequent characters, which reduces the total bits needed.

   ```python
   freq = {}
   for c in string:
       if c in freq:
           freq[c] += 1
       else:
           freq[c] = 1
   ```
   Here, we’re calculating the frequency of each character in the input string, storing it in a dictionary, `freq`, where keys are characters and values are their respective counts.

   ```python
   freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
   ```
   The frequency dictionary is sorted in descending order to prioritize higher-frequency characters for quicker access during the coding process.

### 2. **Creating Tree Nodes**
   ```python
   class NodeTree(object):

       def __init__(self, left=None, right=None):
           self.left = left
           self.right = right

       def children(self):
           return (self.left, self.right)

       def nodes(self):
           return (self.left, self.right)

       def __str__(self):
           return '%s_%s' % (self.left, self.right)
   ```
   This class defines the structure for each node in the Huffman tree. A node can have two children (left and right),
and these children could either be other nodes or characters. The `__str__` method is used to represent the node as a string for debugging or printing.

### 3. **Building the Huffman Tree**
   ```python
   nodes = freq
   ```
   Initially, each character and its frequency are treated as separate nodes.

   ```python
   while len(nodes) > 1:
       (key1, c1) = nodes[-1]
       (key2, c2) = nodes[-2]
       nodes = nodes[:-2]
       node = NodeTree(key1, key2)
       nodes.append((node, c1 + c2))

       nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
   ```
   The code iterates until only one node remains, which will be the root of the Huffman tree:
   - `key1` and `key2` are the two nodes with the smallest frequencies.
   - These nodes are removed from `nodes`, and a new node combining `key1` and `key2` as children is created. 
The combined node’s frequency is the sum of `c1` and `c2`.
   - This new combined node is added back to `nodes`, which is then re-sorted by frequency. The process repeats until the entire tree is built.

### 4. **Generating Huffman Codes**
   ```python
   def huffman_code_tree(node, left=True, binString=''):
       if type(node) is str:
           return {node: binString}
       (l, r) = node.children()
       d = dict()
       d.update(huffman_code_tree(l, True, binString + '0'))
       d.update(huffman_code_tree(r, False, binString + '1'))
       return d
   ```
   The `huffman_code_tree` function recursively traverses the Huffman tree, assigning a binary code to each character:
   - If `node` is a string (leaf node), it’s a character, and `binString` represents its Huffman code.
   - For each recursive call, going left adds '0' to the binary string, and going right adds '1'.
   - The resulting dictionary `d` contains each character and its Huffman code.

### 5. **Printing Huffman Codes**
   ```python
   huffmanCode = huffman_code_tree(nodes[0][0])

   print(' Char | Huffman code ')
   print('----------------------')
   for (char, frequency) in freq:
       print(' %-4r |%12s' % (char, huffmanCode[char]))
   ```
   Finally, the code displays each character and its corresponding Huffman code in a table.

### Example Output (for illustration):
   ```
    Char | Huffman code 
   ----------------------
   'A'  |       0
   'C'  |      10
   'D'  |      11
   'B'  |     110
   ```

This process ensures that the characters with the highest frequency get the shortest binary codes,
which is the essence of **Huffman Coding**. This optimizes the total bit count required to represent the string,
achieving compression without losing any information.

