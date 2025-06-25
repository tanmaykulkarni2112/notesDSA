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
---
# Complex datastructures

## List (Arrays)
These are the dynamic datastructures which can store the values in sequential order, this helps in accessing the element with the help of their indexes. The lists are mutable and are homogenous in nature. 


```python 
list1 = ['ab', 'cd']
list2 = [5,6,7] 
```

### Traversal in lists
We can traverse the lists and we can access them using the indexes, the values or both. Following are the ways of accessing.
```python
l1 = ["apple", "orange", "banana"]
for i in l1: 
    print(i)

for i in range(len(l1)):
    print (l1[i])

for i,v in l1:
    printf(i + "index holds" + v)

for index, value in enumerate(l1):
    print(index)
    print(value)
```

---
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


Here’s a handy list of terminal commands often used when dealing with Python files. These commands help manage files, packages, and the environment effectively:

### **1. General Commands**
- `!ls` – Lists the files and directories in the current working directory (Linux/macOS/WSL).
- `dir` – Similar to `ls`, but for Windows to list the files and directories.
- `!pwd` – Prints the current working directory (Linux/macOS/WSL).
- `cd <directory>` – Changes the current directory.
- `!rm <filename>` – Deletes a file (Linux/macOS/WSL).
- `!mkdir <directory>` – Creates a new directory.

### **2. Managing Python Packages**
- `!pip install <package>` – Installs a Python package.
- `!pip uninstall <package>` – Uninstalls a Python package.
- `!pip list` – Lists all installed Python packages.
- `!pip show <package>` – Displays details of a specific installed package.
- `!pip freeze > requirements.txt` – Saves all current dependencies to `requirements.txt`.

### **3. Running Python Scripts**
- `python <filename>.py` – Runs the specified Python script.
- `python -m <module>` – Runs a module as a script (e.g., `python -m http.server`).

### **4. Virtual Environments**
- `python -m venv <env_name>` – Creates a new virtual environment.
- `source <env_name>/bin/activate` – Activates the virtual environment (Linux/macOS).
- `<env_name>\Scripts\activate` – Activates the virtual environment (Windows).
- `deactivate` – Deactivates the virtual environment.

### **5. File Manipulation & Output**
- `!cat <file>` – Displays the contents of a file (Linux/macOS/WSL).
- `type <file>` – Displays file contents (Windows equivalent of `cat`).
- `!cp <source> <destination>` – Copies a file (Linux/macOS/WSL).
- `!mv <source> <destination>` – Moves or renames a file (Linux/macOS/WSL).

### **6. Debugging and Linting**
- `python -m pdb <filename>.py` – Runs the Python debugger for a script.
- `!flake8 <filename>.py` – Performs linting on a Python file (if `flake8` is installed).
- `!pylint <filename>.py` – Another linting tool for Python scripts.
