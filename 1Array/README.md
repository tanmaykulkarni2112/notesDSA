# Storing in Dict (Hashmap) 

- Store val : index


for index, val in enumerate(datastructre)

dict accessing using index like dict1[key]

to keep tabs, we can make use of the frequency array while dealing with the strings, them being the key for the dictionary 

The tuple is hashable, list is not
The dict is also hashable

## List comprehension

```python
l = [x for x in range(5)]
# OP [0,1,2,3,4]
```

```python
l = [x for x in range(5) if (x % 2) == 0]
# OP [0,2,4]
```

```python
l = [x**2 for x in range(5) if (x % 2) == 0]
# OP [0,4,16]
```

```python
l = [ if (x % 2) == 0 else 5 for x in range(5)]
# OP [0,5,2,5,4]
```

```python
l = [0 * 5]
# op -> [0,0,0,0,0]
```

```python
l1 = [0 * 5]
l2 = [1,2,3]
# op -> [0,0,0,0,0,1,2,3]
```

### This helps in looping through multiple things
```python
for i, j in zip(range(3), range(2,5))
# OP -> 0 2
# 1 3
# 2 4

# Example 2: Using zip with list comprehension and print
pairs = [(x, y) for x, y in zip(range(2), range(3, 7))] 
# [] for list {} for dict
print("Generated pairs:", pairs)


# This will output:
# Generated pairs: [(0, 3), (1, 4)]

```
Sure! Let's break this down more effectively:

### 1. `chr()` – Converts an ASCII value to its corresponding character
- **What it does**: Takes an integer (ASCII value) and returns the character associated with that value.
- **Example**:
    ```python
    print(chr(65))  # Output: 'A'
    print(chr(97))  # Output: 'a'
    print(chr(48))  # Output: '0'
    ```
    - Here, ASCII value `65` corresponds to the letter `'A'`, `97` to `'a'`, and `48` to `'0'`.

### 2. `ord()` – Converts a character to its ASCII value
- **What it does**: Takes a single character and returns its ASCII value.
- **Example**:
    ```python
    print(ord('A'))  # Output: 65
    print(ord('a'))  # Output: 97
    print(ord('0'))  # Output: 48
    ```
    - Here, `'A'` translates to ASCII value `65`, `'a'` to `97`, and `'0'` to `48`.


lambda function