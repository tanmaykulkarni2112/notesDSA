# Python 
- Python is loosely (dynamic) typed  lanuage so there becomes to need of declaring the datatypes of the variables.

```python
example = "demo"
print(example)
# Here example is variable of str (String type)
example = 12
print(example)
# We changed the datatype to int
ex = example
ex = float(ex)
print(ex)
```

- Python is pseudo Object oriented and provides flexibility.

- The datatypes in Python are 
    - int
    - float
    - str
    - bool
    - list
    - dict
    - tuple
    - set
    - class

- Unlike the other language we have keywords like `is`, `in`, `and` & `or` in python!

---

## Conditional statements

Similar to other languages the if else and else if is present too. The difference lies in using else if here the `else if == elif`

To ensure we are using the conditional statement we want to place the code within proper indentation and the keyword ends with `:`

```python

age = 12

if age > 18:
    print("Adult")
elif:
    age < 0:
    print("Unreal age")
else: 
    print("Minor") # This is executed

```

The swtich statement is often used when we dont want to make multiple uses of the if else in python.

The swtich takes the variable and is initated for that datatype. WE MUST USE THE `match` keyword for this purpose! And the defualt is used as `_` 

```
command = "demo"

match command:
    case "begin":
        print("We started the process")
    case "demo":
        print("Demo in progress")
    case "end":
        print("Process ended")
    case _:
        print("Default case executed")
```

## Looping methods in Python

### Range

The range is the function that is used when mostly dealing with the loops. 
> When we place some number in the range -> We are generated the range from `0 to number - 1` if start is not mentioned

In order to place the starting we must provide 2 parameters inside the function `example -> range(1, 6)`

The cannot use the range directly inorder to perform operation we must store it in some datastructure.

```python

print(list(range(1,5)))
# OP -> [1,2,3,4]

# Without mentioning the start
print(list(range(4)))
# The output will be [0,1,2,3]

```

## **For Loops in Python**

The `for` loop in Python is a way to iterate over a sequence or range of values. It's commonly used when you know the number of iterations in advance.

> The `for` loop in Python doesn't require a list or any data structure to operate—it can directly use `range()` or other iterable objects.

#### Example:
```python
# Using a for loop to print numbers from 0 to 4
for i in range(5):
    print(f"Value of i: {i}")
```
**Output:**
```
Value of i: 0
Value of i: 1
Value of i: 2
Value of i: 3
Value of i: 4
```

#### Advanced Example:
```python
# Using a step value in the range to control the loop
for i in range(0, 10, 2):
    print(f"Skipping by 2, value: {i}")
```
**Output:**
```
Skipping by 2, value: 0
Skipping by 2, value: 2
Skipping by 2, value: 4
Skipping by 2, value: 6
Skipping by 2, value: 8
```

#### Points to Note:
- The `for` loop ends automatically when it reaches the end of the sequence or range.
- The `range()` function allows you to define start, end, and step values for customized iteration.

## **While Loops**

The `while` loop is used to repeatedly execute a block of code as long as a specific condition evaluates to `True`. Unlike the `for` loop, the `while` loop doesn't rely on a predetermined sequence; instead, it depends on a condition that could change dynamically during execution.

#### Syntax:
```python
while condition:
    # Code block
    # Typically, the condition will eventually change to False to end the loop.
```

#### Simple Example:
```python
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count to avoid an infinite loop
```
**Output:**
```
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```

#### Key Features:
1. **Dynamic Condition:** The loop continues as long as the condition remains `True`.
2. **Infinite Loops:** Be cautious—if the condition never becomes `False`, the loop runs forever.
   ```python
   while True:
       print("Infinite loop!")  # Manually break using `Ctrl+C` or code logic
   ```
3. **Break Statement:** You can forcefully exit a loop using `break`.
   ```python
   count = 0
   while count < 10:
       if count == 5:
           break  # Exit the loop early
       print(count)
       count += 1
   ```

#### Why Use While Loops?
- Ideal for situations where the number of iterations isn't known beforehand.
- Commonly used in dynamic scenarios like waiting for user input or monitoring changes in a variable.


In Python, apart from `for` and `while` loops, there are a few creative ways to achieve iteration without explicitly using looping constructs:

## **⭐ Using Recursion**
Recursion is when a function calls itself to repeatedly perform a task. Though not strictly a "loop," it's a functional programming approach to iteration.

Example:
```python
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)  # Function calls itself
    else:
        print("Blastoff!")

countdown(5)
```
Output:
```
5
4
3
2
1
Blastoff!
```

## **in** keyword
The in keyword deals with the datastructres when we want to check for the presence of the element in some datastructure like

- character in str
- element in a list 
- key inside the dict

```python

ex = [1,2,3]
print(1 in ex) # returns True
print(0 in ex) # return False

ex_str = "hello"
print('h' in ex_str)  # Returns True
print('z' in ex_str)  # Returns False

```
---

## **is** keyword

The is keyword is typically used when dealing with the compound datastructures like the list, tuples, etc.
> The `is` keyword return true when the data are pointing to same memory.

```python

ex1 = [1,2,3, 10]
ex2 = ex1
print(ex1 is ex2) #  returns True
ex3 = [1,2 ,3, 10]
print(ex1 is ex2) # return False


```

### Why does this happen?
- ex2 is assigned directly to ex1, so both variables refer to the same list object in memory.
- ex3 is created separately, even though it has identical values to ex1, it's stored at a different memory location.

---
## **and** keyword

---
## **or** keyword
