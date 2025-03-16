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
