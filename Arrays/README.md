# Array

When dealing with arrays in **Data Structures and Algorithms (DSA)**, there are a few key concepts we need to understand beforehand.  

### What is an Array?

An **array** is a data structure that stores a **fixed-size**, **sequential collection of elements** of the **same data type**.  
> ⚠️ Note: Arrays store **homogeneous** data, *not heterogeneous*

In **Java**, once an array is created, its size **cannot be changed**. This makes arrays a **static** data structure in terms of size.

Arrays in Java are **zero-indexed**, meaning the index of the first element is `0`. So, if you create an array of size 4, the valid indices will be: `[0, 1, 2, 3]`.

---

### Declaring and Using Arrays in Java

Here’s how we can declare, initialize, update, and access an array in Java:

```java
public class First {
    public static void main(String[] args) {
        // 1. Declaration and initialization of the array
        int[] arr = new int[5];  // Array of integers with size 5

        // 2. Allocation of a value to an index
        arr[1] = 3;

        // 3. Updating/replacing a value at a specific index
        arr[1] = 33;

        // 4. Accessing elements using enhanced for loop
        for (int val : arr) {
            System.out.println(val);
        }
    }
}
```

---

### Explanation of Key Parts:

1. **`int[] arr`**: Declares an array of integers.
2. **`new int[5]`**: Allocates memory for 5 integers. All elements are initialized to `0` by default.
3. **`arr[1] = 3;`**: Assigns the value `3` to the second element (index 1).
4. **`arr[1] = 33;`**: Replaces the value at index 1 with `33`.
5. **`for (int val : arr)`**: Enhanced for-loop (for-each loop) to iterate through array elements and print them.

---

### Additional Notes:

- Trying to access an index outside the bounds of the array (like `arr[5]` in this example) will throw an `ArrayIndexOutOfBoundsException`.
- Arrays can also be initialized directly with values, like:  
  ```java
  int[] numbers = {10, 20, 30, 40};
  ```
- Arrays can store other types like `char[]`, `double[]`, `String[]`, etc., but all elements must be of the same type.


## Type 1:  Index marking

The technique can be used for the problems like - 

- Finding missing numbers
- Detecting duplicates
- Finding the first positive missing number
- Cycle detection (like Floyd’s Tortoise and Hare algorithm)

Let’s break down the **intuition** behind it.

---

## 🧠 Intuition Behind Marking Indices in DSA

### ✨ Core Idea:
Arrays are **indexed structures** — and many problems give us elements that fall **within the range of indices** of the array itself.  
So instead of using **extra space** (like a HashSet), we **reuse the array itself** for tracking.

---

### 📌 Common Scenario:
If you are given:
- An array of size `n`
- And elements in the range `[1, n]` or `[0, n-1]`

Then the index can be used to mark the **presence**, **frequency**, or **status** of the numbers.

---

### 🧪 Techniques to Mark Indexes:

1. **Negation Method**  
   - Flip the number at a particular index to **negative** to indicate the number is "visited".
   - Useful in:  
     - Finding duplicates
     - Finding missing numbers

   #### Example:
   ```java
   for (int i = 0; i < nums.length; i++) {
       int index = Math.abs(nums[i]) - 1;
       nums[index] = -Math.abs(nums[index]); // mark visited
   }
   ```

2. **Increment Method (Cyclic Sort / Count)**  
   - Add `n` or some multiple to mark counts or visits
   - Can use modulo or division to retrieve original values

   #### Example:
   ```java
   int index = nums[i] % n;
   nums[index] += n;  // increase count
   ```

3. **Cyclic Sort**  
   - Rearrange elements such that `nums[i] == i + 1`
   - If not, that index holds the missing number or duplicate

   #### Example:
   ```java
   while (nums[i] != nums[nums[i] - 1]) {
       swap(nums, i, nums[i] - 1);
   }
   ```

---

### 🤔 Why It Works?

Because you're **mapping the value to its corresponding index**, you're creating a **value-index relationship** without extra space.  
This is a form of **in-place hashing**.

Think of the array as a board with cells (indices), and every number wants to go to its correct "home." If a number is already there — it's a duplicate. If a number never reached — it's missing.

---

### ✅ Benefits:
- **O(1) space** (in-place)
- **O(n) time** (usually linear)
- Avoids extra data structures like HashSets or Maps

---
Absolutely — I’ll just add more relevant LeetCode problems that use the index marking method. Here's the updated section with a few more questions added, as you asked:

---

### 🔍 Common Problems to Practice:
- [ ] [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- [ ] [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
- [ ] [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
- [ ] [Set Mismatch](https://leetcode.com/problems/set-mismatch/)
- [ ] [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
- [ ] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) *(slightly related with index usage when optimized)*
- [ ] [Find the Duplicate and Missing Number](https://leetcode.com/problems/set-mismatch/)

---
