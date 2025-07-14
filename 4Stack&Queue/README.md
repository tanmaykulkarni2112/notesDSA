
## 🧠 Monotonic Stack – Core Concept

Monotonic stacks are a specialized form of stacks used to maintain elements in a specific order, which allows solving range-based comparison problems in linear time.

---

### 🧱 Definition

A **monotonic stack** is a stack that maintains a **monotonic order** (either increasing or decreasing) as you process elements:

* **Monotonically increasing stack**:

  * Accepts **smaller or equal** elements
  * **Pops** when a **larger** element is found
* **Monotonically decreasing stack**:

  * Accepts **larger or equal** elements
  * **Pops** when a **smaller** element is found

---

### 🎯 Why Use It?

Used in problems like:

* Next greater element
* Previous smaller element
* Stock span
* Trapping rain water
* Sliding window minimum/maximum

They help reduce **O(n²)** brute force comparisons to **O(n)** by leveraging the stack to remember relevant comparisons.

---

## WITHOUT STORING [VALUE, INDEX] pair

### 🔁 General Pattern (Increasing Stack)

```python
stack = []

for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        prev_index = stack.pop()
        # Do something with arr[i] and arr[prev_index]
    
    stack.append(i)
```

---

### 🔁 General Pattern (Decreasing Stack)

```python
stack = []

for i in range(len(arr)):
    while stack and arr[i] < arr[stack[-1]]:
        prev_index = stack.pop()
        # Do something with arr[i] and arr[prev_index]

    stack.append(i)
```

---

### 🧠 Tip

The stack stores **indices** or `[value, index]` pairs, so you can:

* Compare current value to previous one
* Calculate relative positions (e.g., distance, span)

### EXAMPLE OF `[VALUE, INDEX]`
```
stack = []

for i in range(len(arr)):
    while stack and arr[i] > arr[-1][1]:
        prev_index, prev_value = stack.pop()
        # Do something with arr[i] and arr[prev_value]

    stack.append(i)
```
📌 Important Notes

    ✅ If you store [value, index], compare with stack[-1][0] (value)
    ✅ If you store [index, value], compare with stack[-1][1] (value)

---

Use monotonic stacks to **efficiently track the "next" or "previous" smaller/larger values** without rechecking the entire array each time.

