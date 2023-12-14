from Stack import Stack

# creating a stack
myStack = Stack()

# pushing values 10, 20, 30
myStack.push(10)
myStack.push(20)
myStack.push(30)

# printing / PEEKING into a stack
myStack.peek()

# pushing 40, 50, 60 into the stack
myStack.push(40)
myStack.push(50)
myStack.push(60)
print()
myStack.peek()

# deleting / POPPING vales from a stack
myStack.pop()
myStack.pop()
print()
myStack.peek()

# pushing multiple values into stack
myStack.pushes(100, 200, 300)
print()
myStack.peek()

# popping multiple values
myStack.pops(5)
print()
myStack.peek()

# deleting stack
print()
myStack.__del__()


"""
Output: 

30
20
10

60
50
40
30
20
10

40
30
20
10

300
200
100
40
30
20
10

20
10

Stack Deleted
Stack Deleted
"""