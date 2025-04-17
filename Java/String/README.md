# String

> **Strings** are one of the most common data structures in Java. They are enclosed in **double quotes (`"`)**.

Unlike some languages where strings are primitive or built-in types, **in Java, `String` is a class** — specifically the `String` class in `java.lang`.  
So, strings are **objects**, and their declaration follows the object-oriented syntax just like `ArrayList`, `HashSet`, etc.

---

## 📌 Template for String Declaration

```java
String str = new String("Hello");
```

This is valid, but in practice, the simpler and **more common** way is:

```java
String str = "Hello";  // Preferred
```

---

### ⚠️ Note:
- Both `String str = "Hello";` and `String str = new String("Hello");` work.
- But the second version (`new String(...)`) creates a new object in memory — which is **usually unnecessary** due to Java's **String pool optimization**.
- So the first version is more memory-efficient and idiomatic.

---

## ✅ Summary

| Style | Usage | Notes |
|-------|-------|-------|
| `String str = "Hello";` | ✅ Preferred | Uses string pool (efficient) |
| `String str = new String("Hello");` | 😐 Works, but avoid unless needed | Always creates a new object |

---
Awesome! Let’s get into the juicy stuff. Java Strings have some cool behind-the-scenes behavior thanks to the **String Pool**, **immutability**, and **interning** — all of which help with performance and memory efficiency.

---

## 🔐 Java Strings: Immutability, String Pool, and Interning

---

### 🧊 1. **Immutability**

In Java, **Strings are immutable** — once created, they **cannot be changed**.

```java
String s = "hello";
s = s + " world";  // This doesn't modify the original string — it creates a new one
```

#### 🧠 Why this matters:
- Thread-safe
- Hashing is consistent (useful for keys in HashMaps)
- Safe sharing of string references

---

### 🏊 2. **String Pool**

Java maintains a **special memory area called the *String Pool*** (aka *intern pool*), which stores **unique string literals**.

```java
String a = "hello";
String b = "hello";
System.out.println(a == b);  // true → both point to the same object in the pool
```

When you use a literal (like `"hello"`), Java checks the pool:
- If it exists → reuse it
- If not → add it

---

### 🆕 3. **Using `new String()` skips the pool**

```java
String a = "hello";
String b = new String("hello");

System.out.println(a == b);       // false → different objects
System.out.println(a.equals(b));  // true → content is same
```

✅ `.equals()` compares **contents**  
❌ `==` compares **references**

---

### 🧪 4. **String Interning (`.intern()`)**

You can **manually intern** a string using `.intern()` to ensure it's in the pool.

```java
String a = new String("hello");
String b = a.intern();

String c = "hello";

System.out.println(b == c);  // true → both now point to the interned string
```

---

### 📌 Summary Table

| Concept       | What It Means                                  | Why It Matters                         |
|---------------|--------------------------------------------------|-----------------------------------------|
| **Immutable** | Cannot change after creation                     | Safe, consistent, thread-safe           |
| **String Pool** | Java stores string literals in a shared pool   | Saves memory                            |
| **`new String()`** | Always creates a new object                | Avoid unless necessary                  |
| **`.intern()`** | Forces a string into the pool                 | Ensures reference equality for literals |

---
## ✅ What Actually Happens:
### 1. new String("hello")

- Always creates a new object in the heap, regardless of whether "hello" exists in the string pool.

- This object has the same value as the literal "hello" but is a different object in memory.

### 2. "hello" (a string literal)

- Is stored in the String Pool, which is a part of the method area (historically part of the permgen/metaspace depending on Java version), not regular heap.

- It’s shared, reused, and managed by the JVM for efficiency.

### 3. intern()

- If the pool already has the string, returns a reference to it.

- If not, adds the string to the pool and returns the pooled reference.

## 🔥 Example: When intern() is helpful
```java

String s1 = "hello";
String s2 = new String("hello");

System.out.println(s1 == s2);           // false
System.out.println(s1 == s2.intern());  // true ✅

```
### 🧠 Why use .intern() here?
To force s2 (a heap object) to reference the pooled version of "hello" — making it possible to use == for comparison.


# 🧠 TYPE 1 : Frequency Counter Pattern (In array too)
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
