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

    public static int[] arrayReturn () {
            return new int[] {9, 10, 11}; // another way of returning array
        }

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

        // Printing the returned array
        int returnArr[] = arrayReturn(); // Store in new array to access 
        for(int val : returnArr) {
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


## **Type 1:  Index marking**

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

# 🧠 TYPE 2 : Java Lexicographical Order

## 🔹 Basics of Lexicographical Order
- Works like dictionary order
- Compare character-by-character (Unicode value)
- In Java: `str1.compareTo(str2)`
  - Returns < 0 → str1 < str2
  - Returns = 0 → str1 == str2
  - Returns > 0 → str1 > str2

---
## 🔸 Common LeetCode Problems & Patterns

### 1. **Next Permutation**
- **Problem**: [Leetcode 31 - Next Permutation](https://leetcode.com/problems/next-permutation/)

---

### 2. **All Lexicographical Permutations**
- **Problem**: [Leetcode 46 - Permutations](https://leetcode.com/problems/permutations/) / [Leetcode 47 - Permutations II](https://leetcode.com/problems/permutations-ii/)

---

### 3. **Alien Dictionary**
- **Problem**: [Leetcode 953 - Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)

---

### 4. **K-th Permutation**
- **Problem**: [Leetcode 60 - Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

---

### 5. **Lexicographically Smallest Subsequence**
- **Problems**:
  - [Leetcode 316 - Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
  - [Leetcode 1081 - Smallest Subsequence](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

---

## 🔸 Quick Tips
- Always sort input if question asks for lex order
- Use `compareTo()` for string comparisons
- Convert numbers to string (`String.valueOf(num)`) for lexicographical comparisons

---

## 📌 Related Java Methods
- `String.compareTo(String)`
- `Arrays.sort()`
- `Collections.sort()`
- `PriorityQueue` with custom comparator

---


# 🧠 TYPE 3 : Store are you go (HashMap-Based Problems)

## 🔹 Intuition:
> "I’m iterating, and I want to know **if I’ve seen something before** (or its complement / match / condition)."
> Usually uses a HashMap or HashSet to store values as you go.

---

## 🔸 Problem List:

1. [Leetcode 1 - Two Sum](https://leetcode.com/problems/two-sum/)
2. [Leetcode 167 - Two Sum II (Sorted)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
3. [Leetcode 560 - Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
4. [Leetcode 523 - Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
5. [Leetcode 1099 - Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/)
6. [Leetcode 15 - 3Sum](https://leetcode.com/problems/3sum/)
7. [Leetcode 16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
8. [Leetcode 18 - 4Sum](https://leetcode.com/problems/4sum/)
9. [Leetcode 653 - Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
10. [Leetcode 532 - K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)
11. [Leetcode 1679 - Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)
12. [Leetcode 217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

# 🧠 TYPE 4 : Two Pointers - In-Place Rearrangement
## 🧠 What It Is
A pattern where two pointers are used to rearrange elements **in-place**, usually to:
- Filter values
- Shift/move elements
- Maintain relative order

Usually done in **O(n)** time and **O(1)** space.

---

## 📌 Common Use Cases

### 1. **Remove Elements / Filter Values**
- [Leetcode 27 - Remove Element](https://leetcode.com/problems/remove-element/)

### 2. **Move Zeros / Shift Elements**
- [Leetcode 283 - Move Zeroes](https://leetcode.com/problems/move-zeroes/)

### 3. **Segregate Even and Odd / 0s and 1s**
- [Leetcode 905 - Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)
- [Leetcode 75 - Sort Colors (Dutch National Flag)](https://leetcode.com/problems/sort-colors/)

### 4. **Remove Duplicates from Sorted Array**
- [Leetcode 26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [Leetcode 80 - Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

### 5. **Partition Array Around a Pivot**
- [Leetcode 215 - Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### 6. **Reverse an Array / Part of It**
- [Leetcode 344 - Reverse String](https://leetcode.com/problems/reverse-string/)
- [Leetcode 541 - Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

### 7. **Rotate Array**
- [Leetcode 189 - Rotate Array](https://leetcode.com/problems/rotate-array/)

### 8. **Flatten Arrays / Merge Intervals**
- [Leetcode 56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### 9. **Sort Colors (Dutch National Flag Problem)**
- [Leetcode 75 - Sort Colors](https://leetcode.com/problems/sort-colors/)

### 10. **Sliding Window Setup**
- [Leetcode 283 - Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [Leetcode 26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

# prefix tracking/ sliding window

Absolutely! This pattern is most commonly known as:

> ### 🔑 **"Frequency Counter" Pattern**  
But you can totally think of it as:
- **Frequency Array** → when using `int[]`
- **Frequency Map** → when using `HashMap<Char, Int>`

---
# 🧠 TYPE 5 : Frequency Counter Pattern
A common pattern where you **count occurrences of characters or elements**, typically in strings or arrays. Useful for comparison, inclusion checks, anagrams, and permutations.

---

## ✅ When to Use
- Comparing two strings or arrays
- Checking if one string can be formed from another
- Validating anagrams or permutations
- Sliding window character matching

---

## 📦 Data Structures
| Type            | When to Use                                      |
|-----------------|--------------------------------------------------|
| `int[26]`       | When working with lowercase English letters only |
| `HashMap`       | When characters or keys are variable or Unicode  |

---

## ⚙️ Core Idea

1. Count elements from one source
2. Use the frequency info to compare or validate the second source

---

## 🔁 Common Problems

| Problem | Type |
|--------|------|
| [383. Ransom Note](https://leetcode.com/problems/ransom-note/) | Can one string be built from another |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Compare char frequency |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Group by frequency signature |
| [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Sliding window + match frequency |
| [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding window anagrams |
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Advanced: sliding window + freq map |

---

## ✨ Template (with Array)
```java
int[] freq = new int[26];  // for lowercase letters

// Count frequency
for (char ch : str.toCharArray()) {
    freq[ch - 'a']++;
}

// Use frequency
for (char ch : otherStr.toCharArray()) {
    if (freq[ch - 'a'] == 0) return false;
    freq[ch - 'a']--;
}
```

---

## ✨ Template (with HashMap)
```java
Map<Character, Integer> map = new HashMap<>();

// Count frequency
for (char ch : str.toCharArray()) {
    map.put(ch, map.getOrDefault(ch, 0) + 1);
}

// Use frequency
for (char ch : otherStr.toCharArray()) {
    if (!map.containsKey(ch)) return false;
    if (map.get(ch) == 1) map.remove(ch);
    else map.put(ch, map.get(ch) - 1);
}
```

---

##  Pro Tip
Use `int[26]` for speed and simplicity **if the character set is known and small**. Use `HashMap` when flexibility is needed.

---
Awesome! Here’s your updated **Type 6** entry in the official cheatsheet style — now cleanly split into **Type 6A** and **6B**, covering both single and double element cases. Let's lock it in 💼✨

---

# 🧠 **Type 6 – Remove From Ends (Target Element Based)**

### 🧩 Core Idea
You’re allowed to **remove elements only from the ends** (left or right), and your goal is to:
- Either **remove a specific target** (like `x`, a sum, or a value), or
- **Eliminate two specific elements** (like `min` and `max`),
- While **minimizing the number of operations**.

---

### 🔹 **Type 6A – Remove One Element / Target Value**
> 🟨 Useful when you must remove elements from ends to hit a **target condition** (e.g., sum = `x`)

#### ✅ Common Examples
| Problem | Link | Description |
|--------|------|-------------|
| **Leetcode 1658 – Minimum Operations to Reduce X to Zero** | [🔗](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | Remove from ends until remaining sum is `x`. Try all prefix+suffix combos. |
| **GFG – Min deletions to make sum divisible by K** | [🔗](https://www.geeksforgeeks.org/minimum-deletions-make-sum-divisible-k/) | Remove from ends to reach a valid modulo condition. |

#### 🧠 Strategy
- Precompute **prefix sums** and **suffix sums**.
- Use a **map** or **two-pointer** approach to find where `prefix + suffix = target`.
- Track and return **minimum number of deletions**.

---

### 🔹 **Type 6B – Remove Two Key Elements (min & max)**
> 🟩 Classic when you must **remove both `min` and `max`**, only from ends.

#### ✅ Common Examples
| Problem | Link | Description |
|--------|------|-------------|
| **Leetcode 2091 – Removing Min and Max** | [🔗](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) | Remove both `min` and `max` by trying all combinations (L, R, Both). |
| **GFG – Make array good by removing min/max** | [🔗](https://www.geeksforgeeks.org/minimum-deletions-make-array-good/) | Similar idea but with condition on array content.

#### 🧠 Strategy
1. Find `minIdx` and `maxIdx`
2. Try all 3 removal paths:
   - Remove both from **left**
   - Remove both from **right**
   - Remove one from **left**, one from **right**
3. Return `min(left, right, bothSides)`

#### 🧪 Code Snippet
```java
int left = Math.max(minIdx + 1, maxIdx + 1);
int right = Math.max(n - minIdx, n - maxIdx);
int both = (minIdx + 1) + (n - maxIdx);
return Math.min(left, Math.min(right, both));
```

---

### ✅ When to Recognize This Pattern:
- You **can’t remove from middle** — only ends are allowed.
- You have **specific targets** to eliminate (`min`, `max`, sum = x).
- Try **prefix + suffix** combinations OR simulate smart index cuts.
