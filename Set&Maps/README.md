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
   - `in`: Checks if an item is in the set (`if 2 in myset`).

#### Example Code:
```python
myset = set()  # Correct way to initialize
myset.add(2)
myset.add(1)
myset.add(7)
myset.add(2)  # Duplicate, won't be added

if 2 in myset:
    print(2)  # Output: 2

myset.remove(2)  # Removes 2 from the set

# Creating a set from a string
string = "ajhysvafjkn bfkaubsfasfbausbfnaks"
strset = set(string)  # Removes duplicates

# Looping through a set
for s in strset:
    print(s)  # Prints unique characters in any order
```

---

### **Hashmap (Dictionaries)**
A **dictionary** in Python is a collection of key-value pairs. Keys are unique, and values can be of any type.

#### Key Notes:
1. **Initialization:**
   - Dictionaries can have various hashable data types as keys, like strings, integers, or tuples.
   - Example:
     ```python
     d = {1: "Hello", 2: "BYE"}  # Integer keys
     dict2 = {(1, 2, 3, 4): "tuple hashed", "key2": "str hashed"}  # Tuple and string keys
     ```

2. **Common Dictionary Methods:**
   - `d.keys()`: Returns all the keys in the dictionary.
   - `d.values()`: Returns all the values in the dictionary.
   - `d.items()`: Returns key-value pairs as tuples.

#### Example Code:
```python
d = {1: "Hello", 2: "BYE"}
dict2 = {(1, 2, 3, 4): "tuple hashed", "key2": "str hashed"}
print(dict2["key2"])  # Output: str hashed

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
default[2] = 645
print(default[5])  # Output: 0 (default value for `int`)
```

#### **Counter (from `collections`)**
A `Counter` is a specialized dictionary for counting occurrences of items (e.g., characters in a string).
```python
from collections import Counter

str1 = "acdacdcacdcsgrgsacdcavfersacd"
counter = Counter(str1)
print(counter)  
# Output: {'a': 6, 'c': 7, 'd': 6, ...} (frequency of each character)
```

---
