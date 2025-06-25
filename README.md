# Essentials

## Sorting 

```python
newArr = sorted(arr) # New sorted array
arr.sort() # Inplace sorting

string = "Tanmay" # STRING CAN BE ONLY SORTED THIS WAY
sortedStr = sorted(string)
```


## Map 

```python
# NOTE THAT ONLY TUPLES ARE HASHABLE

map.items() # {both}
map.keys()
map.values()

# ---
map = {}
key = 'ABC'
if 'ABC' in map:
    map['ABC'].append(0)
else :
    map['ABC'] = 0
```

### ⭐Initializing the empty Array where can append freely

```python
arr = [[] for _ in range(4)]
# arr =   [[], [], [], []]
# At index  0  1   2   3

arr[0].append(2) # ✅This will work!
```
### ⭐Inserting when key does not exist

```python
array = []
array[3] = 2113 # ❌ Not allowed

# We should rather do 
array = collections.defaultdict(list)# Default value at key is list []

# --OR--
array = collections.defaultdict(int) # Default value at key = 0
array = collections.defaultdict(set) # Default value at key is set()
array = collections.defaultdict(float) # Default value at key = 0.0
```


## String

```python
string = ""
string += '!' # ✅ Allowed
print(string) #!

# Substring 
bigString = "abcdefgh"
lilString = bigString[0:len(bigString)] #abcdefg
```

