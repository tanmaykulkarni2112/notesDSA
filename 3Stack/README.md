# Stack

> There is not stack datastructure in Python as such so we make use of the List itself.

The following are the methods that we may end up using-

- .append()
- .pop()

The retreival for the item in list will be the same as ever, example say we have `stk[-1] we give us the last item`

## Note

We dont have the method like `.empty()` or `.peek()` in python lists

The following are the patterns that might be seen :- 

1. Valid parenthesis

At the end stack is empty means that the valid parenthesis is present. We push and pop according to the nature of the qustion having the convention of appending on '([{' and popping on '}', ')', ']'. Order matters so we visualize the stack here 