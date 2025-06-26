# Ways of Solving


## 1. Hashing
1. Using HashSet for identifying duplicates
   
2. Use HashSet/ HashMap to note specific number is present or not. `{keep track of index -> map, else Set}`

3. Using map to group similar attributes together

## 2. Two-pointers

**Should always be sorted**

left = 0

right = length - 1

calculatedNumber > target --> right -= 1
calculatedNumber < target --> left += 1 

Can be used together with other topics like prefix values(max/min) noting etc.
 
## 3. Frequency Array  AND `Bubble sort`

`Bubble sort => arr[freq].append(numberWithThatFrequency)`

[In main README](https://github.com/tanmaykulkarni2112/notesDSA/blob/main/README.md)

## 4. Prefix Array

- Sum
- Min / Max

Create a pre/postfix array and then use it.
We can  have `inserting Res[i] and then update the prefix/ postfix` to get optimal results

> We can use it along with 2pointers

## 5. Sliding Window

Favourable condition / Normal logic -> we Increase size window
#### We can use the `hashmap` altogether to keep track of the frequency 


#### In one of the conditions we will have to do l += 1

like when using while loop     
```python
left, right = 0,1 
while (right < len(arr)):
    if:
        # LOGIC
    else:
        left += 1 # left += r
    right += 1
```


when we use for loop 

```python
for r in range(len(arr)):
    # while/ if / else ->  FOR HANDLING L
    # When dealing with set
```

Unfavourable condition -> Reduce the size of window