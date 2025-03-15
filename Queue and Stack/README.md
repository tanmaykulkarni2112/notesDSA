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

### Parenthesis Related Problems  

1. Checking if a given string of parentheses is balanced.  