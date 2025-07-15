### **Sets**
A **set** in Python is an unordered collection of unique items. Sets automatically eliminate duplicate elements, making them extremely useful for tasks like removing duplicates or checking membership efficiently.

#### Key Notes:
1. **Set Initialization:**
   - `myset = {}` creates an empty dictionary, **not an empty set**. To create an empty set, use:
     ```python
     myset = set()
     ```

2. **Methods Used in Sets:**
   - `add(item)`: Adds a single element to the set.
   - `remove(item)`: Removes an element from the set. If the element is not found, it raises a `KeyError`.
   - `discard(item)`: Similar to `remove()`, but doesn’t raise an error if the element isn’t found.
   - `pop()`: Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.
   - `clear()`: Removes all elements from the set.
   - `in`: Checks if an item is in the set (`if 2 in myset`).

#### Set Operations:
- **Union:** `set1.union(set2)` or `set1 | set2` - Returns a new set with all elements from both sets.
- **Intersection:** `set1.intersection(set2)` or `set1 & set2` - Returns a new set with elements common to both sets.
- **Difference:** `set1.difference(set2)` or `set1 - set2` - Returns a new set with elements in `set1` but not in `set2`.
- **Symmetric Difference:** `set1.symmetric_difference(set2)` or `set1 ^ set2` - Returns a new set with elements in either set, but not both.

#### Time Complexity:
- **add, remove, discard, in:** Average case O(1), Worst case O(n)
- **union, intersection, difference:** O(len(s1) + len(s2))

#### When to Use Sets:
- Removing duplicate elements from a list.
- Membership testing (checking if an element is present).
- Performing mathematical set operations like union, intersection, and difference.

#### Example Code:
```python
myset = {1, 2, 3}
myset.add(4)  # {1, 2, 3, 4}
myset.remove(3) # {1, 2, 4}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
```

---

### **Hashmap (Dictionaries)**
A **dictionary** in Python is a collection of key-value pairs. Keys are unique, and values can be of any type.

#### Key Notes:
1. **Initialization:**
   - Dictionaries can have various hashable data types as keys, like strings, integers, or tuples.
   - Example:
     ```python
     d = {1: "Hello", 2: "BYE"}
     ```

2. **Common Dictionary Methods:**
   - `d.keys()`: Returns a view object displaying a list of all the keys.
   - `d.values()`: Returns a view object displaying a list of all the values.
   - `d.items()`: Returns a view object displaying a list of key-value tuple pairs.
   - `d.get(key, default=None)`: Returns the value for a key if it exists, otherwise returns a default value.
   - `d.pop(key)`: Removes the specified key and returns the corresponding value.
   - `d.popitem()`: Removes and returns the last inserted key-value pair as a tuple.

#### Time Complexity:
- **Access, Insert, Delete:** Average case O(1), Worst case O(n)
- **Iteration:** O(n)

#### When to Use Dictionaries:
- Storing and retrieving data with a key.
- Counting frequencies of items.
- Implementing caches or memoization.

#### Example Code:
```python
d = {'a': 1, 'b': 2}
print(d.get('a')) # 1
print(d.get('c', 0)) # 0

d.pop('a') # returns 1 and d becomes {'b': 2}

for key, val in d.items():
    print(f"The key is {key} and the value is {val}")
```

---

### **Advanced Dictionary Features**

#### **DefaultDict (from `collections`)**
A `defaultdict` provides default values for keys that are accessed but not present in the dictionary.
```python
from collections import defaultdict

default = defaultdict(int)
default[1] = 232
print(default[5])  # Output: 0 (default value for int)
```

#### **Counter (from `collections`)**
A `Counter` is a specialized dictionary for counting occurrences of items (e.g., characters in a string).
```python
from collections import Counter

str1 = "acdacdcacdcsgrgsacdcavfersacd"
counter = Counter(str1)
print(counter['a']) # 6
```

---
