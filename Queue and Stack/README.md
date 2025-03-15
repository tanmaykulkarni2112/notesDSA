# Stack 

## Declaration of Stack  
```java
Stack<Character> stk = new Stack<>();
```

## Necessary Methods for Stack Operations  

### 1. `stk.isEmpty()`  
- **Description:** This method checks if the stack is empty.  
- **Returns:** `true` if the stack contains no elements, otherwise `false`.  
- **Example:**  
  ```java
  if (stk.isEmpty()) {
      System.out.println("Stack is empty");
  }
  ```

### 2. `stk.push(element)`  
- **Description:** This method adds an element to the top of the stack.  
- **Parameters:** The element to be pushed onto the stack.  
- **Example:**  
  ```java
  stk.push('(');
  stk.push('{');
  ```

### 3. `stk.peek()`  
- **Description:** This method returns the top element of the stack without removing it.  
- **Returns:** The top element of the stack.  
- **Throws:** `EmptyStackException` if the stack is empty.  
- **Example:**  
  ```java
  char top = stk.peek();
  System.out.println("Top element: " + top);
  ```

### 4. `stk.pop()`  
- **Description:** This method removes and returns the top element of the stack.  
- **Returns:** The element removed from the stack.  
- **Throws:** `EmptyStackException` if the stack is empty.  
- **Example:**  
  ```java
  char removed = stk.pop();
  System.out.println("Popped element: " + removed);
  ```

### 5. `stk.size()`  
- **Description:** This method returns the number of elements currently in the stack.  
- **Returns:** The size of the stack as an integer.  
- **Example:**  
  ```java
  int size = stk.size();
  System.out.println("Stack size: " + size);
  ```

---
Here is the exact **Markdown (`.md`) content** with proper formatting:  

# Stack Patterns in LeetCode

Stacks are a fundamental data structure in **LeetCode**, and several common **patterns** revolve around their usage.  

---

## 1. Monotonic Stack (Increasing / Decreasing)
📌 **Used for: Finding next/previous greater or smaller elements efficiently.**  
🔹 **Key Idea**: Maintain a stack of **indices** or **values** in increasing/decreasing order.  
🔹 **Time Complexity**: **O(n)** (Each element is pushed/popped at most once).  

### Problems Using Monotonic Stack
✅ **Next Greater Element** (**LeetCode 496, 503, 556**)  
✅ **Daily Temperatures** (**LeetCode 739**)  
✅ **Largest Rectangle in Histogram** (**LeetCode 84**)  
✅ **Trapping Rain Water (Stack Approach)** (**LeetCode 42**)  

**Example: Next Greater Element**
```java
public int[] nextGreaterElements(int[] nums) {
    int n = nums.length;
    int[] res = new int[n];
    Stack<Integer> stack = new Stack<>();
    
    Arrays.fill(res, -1); // Default to -1
    for (int i = 0; i < 2 * n; i++) {  // Circular array
        while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
            res[stack.pop()] = nums[i % n];
        }
        if (i < n) stack.push(i);
    }
    return res;
}
```
🔹 **Why Monotonic Stack?**  
- Helps track **next/previous greater or smaller elements** in **O(n) time**.
- Works great for **spans, temperature, and stock price** problems.

---

## 2. Index-Based Stack for Substring/Range Calculations
📌 **Used for: Finding valid substrings, spans, or range-based calculations.**  
🔹 **Key Idea**: Store **indices** instead of actual values in the stack.  
🔹 **Time Complexity**: **O(n)**.  

### Problems Using Index-Based Stack
✅ **Longest Valid Parentheses** (**LeetCode 32**)  
✅ **Online Stock Span** (**LeetCode 901**)  
✅ **Largest Rectangle in Histogram** (**LeetCode 84**)  

**Example: Longest Valid Parentheses**
```java
public int longestValidParentheses(String s) {
    int maxLen = 0;
    Stack<Integer> stack = new Stack<>();
    stack.push(-1);  // Base index
    
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.isEmpty()) {
                stack.push(i);
            } else {
                maxLen = Math.max(maxLen, i - stack.peek());
            }
        }
    }
    return maxLen;
}
```
🔹 **Why Index-Based Stack?**  
- Allows efficient **substring length calculations**.
- Helps track **open and closing brackets**.

---

## 3. Backtracking with Stack (DFS Simulation)
📌 **Used for: Tree traversals, generating valid sequences, and graph problems.**  
🔹 **Key Idea**: Use a **stack instead of recursion** to simulate DFS traversal.  
🔹 **Time Complexity**: **O(n)** (depends on problem).  

### Problems Using Stack for DFS
✅ **Binary Tree Preorder/Inorder/Postorder Traversal (Iterative)** (**LeetCode 144, 94, 145**)  
✅ **Generate Parentheses** (**LeetCode 22**)  
✅ **Remove Invalid Parentheses** (**LeetCode 301**)  

**Example: Iterative Preorder Traversal**
```java
public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    if (root != null) stack.push(root);

    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        res.add(node.val);
        if (node.right != null) stack.push(node.right);
        if (node.left != null) stack.push(node.left);
    }
    return res;
}
```
🔹 **Why Stack for DFS?**  
- Avoids **recursion depth issues**.
- Works well for **iterative tree traversal**.

---

## 4. Stack for Expression Evaluation & Parsing
📌 **Used for: Evaluating mathematical expressions, postfix/prefix conversions.**  
🔹 **Key Idea**: Use stacks to track **operands and operators**.  
🔹 **Time Complexity**: **O(n)**.  

### Problems Using Stack for Expression Parsing
✅ **Basic Calculator I, II, III** (**LeetCode 224, 227, 772**)  
✅ **Evaluate Reverse Polish Notation** (**LeetCode 150**)  
✅ **Valid Parentheses** (**LeetCode 20**)  

**Example: Evaluate Reverse Polish Notation**
```java
public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
    for (String token : tokens) {
        if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
            int b = stack.pop();
            int a = stack.pop();
            switch (token) {
                case "+": stack.push(a + b); break;
                case "-": stack.push(a - b); break;
                case "*": stack.push(a * b); break;
                case "/": stack.push(a / b); break;
            }
        } else {
            stack.push(Integer.parseInt(token));
        }
    }
    return stack.pop();
}
```
🔹 **Why Stack for Expressions?**  
- Helps evaluate **infix/postfix expressions**.
- Useful for **parsing nested expressions**.

---

## 5. Stack for Backtracking Problems
📌 **Used for: Exploring multiple possibilities using backtracking.**  
🔹 **Key Idea**: Use **stack instead of recursion** to track decisions.  
🔹 **Time Complexity**: Depends on problem (often **O(2^N)**).  

### Problems Using Stack for Backtracking
✅ **Generate Parentheses** (**LeetCode 22**)  
✅ **Letter Combinations of a Phone Number** (**LeetCode 17**)  
✅ **Word Search (Iterative DFS)** (**LeetCode 79**)  

**Example: Generate Parentheses (Backtracking with Stack)**
```java
public List<String> generateParenthesis(int n) {
    List<String> res = new ArrayList<>();
    Stack<StringBuilder> stack = new Stack<>();
    Stack<int[]> countStack = new Stack<>();
    
    stack.push(new StringBuilder());
    countStack.push(new int[]{0, 0});
    
    while (!stack.isEmpty()) {
        StringBuilder sb = stack.pop();
        int[] counts = countStack.pop();
        int open = counts[0], close = counts[1];

        if (sb.length() == 2 * n) {
            res.add(sb.toString());
            continue;
        }
        if (open < n) {
            stack.push(new StringBuilder(sb).append("("));
            countStack.push(new int[]{open + 1, close});
        }
        if (close < open) {
            stack.push(new StringBuilder(sb).append(")"));
            countStack.push(new int[]{open, close + 1});
        }
    }
    return res;
}
```
🔹 **Why Stack for Backtracking?**  
- Avoids **recursive function calls**.
- Helps explore **multiple possibilities iteratively**.

---

## Summary of Stack Patterns in LeetCode
| Pattern | Common Problems | Key Idea |
|---------|---------------|-----------|
| **Monotonic Stack** | Next Greater Element, Daily Temperatures | Maintain increasing/decreasing order |
| **Index-Based Stack** | Longest Valid Parentheses, Stock Span | Store indices instead of values |
| **DFS Simulation** | Tree Traversal (Iterative), Graph DFS | Use stack instead of recursion |
| **Expression Parsing** | Basic Calculator, Reverse Polish Notation | Evaluate expressions using stack |
| **Backtracking with Stack** | Generate Parentheses, Word Search | Replace recursion with stack |
