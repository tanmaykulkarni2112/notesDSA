Recursion is a process where a function calls itself to solve a problem by breaking it down into smaller instances of the same problem. It is commonly used for iterative logic, but instead of explicit loops, it relies on self-referencing function calls.
A recursive function primarily handles two things:
- Data (parameters)—which are essential for computation and define the problem state at each step.
- Memory management (stack frames)—which store the function's execution context, allowing subsequent calls to be processed correctly.
Each recursive call operates on its parameters and occupies a unique memory address. The function continues calling itself until it reaches a base case, where recursion stops. Upon termination, computed values are returned up the call stack.


Before implementing recursion, the function must define a base case, which acts as the stopping condition. The base case ensures that recursion does not continue indefinitely and provides the simplest solution to the problem. Without a proper base case, the function would recurse infinitely, leading to a stack overflow error.
Here’s how we can structure a recursive function:


```python
def factorial(n):
    # Base case: stop recursion when n reaches 1
    if n == 1:
        return 1
    # Recursive case: call the function with a smaller input
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

This function correctly defines the base case (if n == 1: return 1) before proceeding to the recursive call. The function keeps reducing n until it reaches 1, at which point recursion stops, and results propagate back up.

We are dealing with recursive function being called once here so time complexity is O(n). But in problems where recursive function is called 2-3 times the TC will be O(2^n) or O(3^n)

### Recursion can be used in varied datastructures but will be prominently seen in Linkedlists and tree