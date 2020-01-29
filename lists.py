# similar to arrays, can be iterated over, limitless in size, zero-based, can contain any type of variable 
list = []

# can add to a list with .append method
# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. 
list.append("cat")
list.append("bird")
list.append("frog")
list.append("dog")
# so out stack from bottom to top is [cat, bird, frog, dog]
list.pop()
# pop = destructive, so our stack is now [cat, bird, frog]


# can access items by index within bracket notation
first = list[0]

