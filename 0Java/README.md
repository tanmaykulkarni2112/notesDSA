# Essentials 

## 🔗 HashSet, HashMap, LinkedHashSet, and TreeSet (SortedSet)

When working with collections in Java, especially during DSA practice, these data structures come in super handy for efficient lookups, deduplication, and frequency mapping.

---
> ⚠️ **Note:** When working with **collections** in Java, we usually reference them using the **interface type** (like `List`, `Set`, `Map`) rather than the implementing class (like `ArrayList`, `HashSet`). This promotes flexibility and allows access to standard methods across different implementations.

```java
HashMap <Integer,Integer> ourMap = new HashMap <>();
ourMap.put(1,9); // ✅ 
HashMap.put(1, 9); // ❌
```


### ✅ **HashSet**
- Stores **unique elements** (no duplicates allowed).
- **Unordered** — does not guarantee insertion order.
- Backed by a **HashMap** internally.

#### 🔹 Common Methods:
```java
add(E e)         // Adds element if not already present
remove(Object o) // Removes element
contains(Object o) // Checks if element exists
isEmpty()        // Returns true if set is empty
size()           // Returns number of elements
```

#### 🛠 Use Case in DSA:
- Finding duplicates
- Set operations (union, intersection, difference)
- Fast lookup in O(1) average time

---

### ✅ **HashMap**
- Stores **key-value pairs**.
- **Keys are unique**, values can repeat.
- **Unordered** — no guaranteed order of keys.

#### 🔹 Common Methods:
```java
put(K key, V value)         // Add or update key-value pair
get(Object key)             // Retrieve value by key
containsKey(Object key)     // Checks if key exists
containsValue(Object value) // Checks if value exists
remove(Object key)          // Removes key and value
keySet()                    // Returns all keys
values()                    // Returns all values
entrySet()                  // Returns all key-value pairs
```

#### 🛠 Use Case in DSA:
- Frequency maps
- Index mapping
- Caching
- Graphs (Adjacency List)

---

### ✅ **LinkedHashSet**
- Like HashSet but **maintains insertion order**.
- Slightly slower than HashSet due to order tracking.

#### 🔹 Methods:
Same as `HashSet`.

#### 🛠 Use Case in DSA:
- When uniqueness is needed *and* order matters (e.g., LRU Cache implementation)

---

### ✅ **TreeSet (SortedSet)**
- Stores **unique elements** in **sorted order** (natural or custom comparator).
- Backed by a **Red-Black Tree**.
- Operations take **O(log n)** time.

#### 🔹 Common Methods:
```java
add(E e)              // Adds element
ceiling(E e)          // Smallest element >= e
floor(E e)            // Largest element <= e
higher(E e)           // Smallest element > e
lower(E e)            // Largest element < e
first() / last()      // First and last elements
remove(Object o)      // Removes element
```

#### 🛠 Use Case in DSA:
- Range queries
- Floor/ceiling lookups
- Maintaining sorted dynamic data

---

### Quick Comparison Table:

| Feature       | HashSet | HashMap | LinkedHashSet | TreeSet |
|---------------|---------|---------|----------------|---------|
| Duplicates    | ❌       | ❌ (keys) ✅ (values) | ❌              | ❌       |
| Order         | ❌       | ❌       | ✅ Insertion Order | ✅ Sorted |
| Null Support  | ✅ (1 null) | ✅ (1 null key, many null values) | ✅             | ✅ (no null if custom comparator) |
| Time Complexity | O(1)     | O(1)     | O(1)              | O(log n) |

---

Let me know if you want a small code example showing how to use each of these in a DSA context (like counting characters, finding duplicates, etc.)
# notesDSA

### Points to note
1. We for the String `s` we can direct access the character by using the `s.charAt(index)`; 

## Paterns and approaches 

### `Best Substring Search Methods`

| **Use Case**                  | **Best Method**         | **Applied On**       |
|--------------------------------|-------------------------|----------------------|
| Small strings (~10³)           | Brute Force / Sliding Window | Simple substring search |
| Large strings (~10⁵)           | KMP Algorithm           | Exact pattern matching |
| Multiple pattern searches      | Rabin-Karp              | Hash-based matching |
| Finding all occurrences        | Z-Algorithm             | Prefix-based pattern search |
