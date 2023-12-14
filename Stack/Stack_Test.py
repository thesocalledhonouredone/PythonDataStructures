from Stack import Stack

# creating a stack
x = Stack()

# pushing values 10, 20, 30
x.push(10)
x.push(20)
x.push(30)

# printing / PEEKING into a stack
x.peek()

# pushing 40, 50, 60 into the stack
x.push(40)
x.push(50)
x.push(60)
print()
x.peek()

# deleting / POPPING vales from a stack
x.pop()
x.pop()
print()
x.peek()

# pushing multiple values into stack
x.pushes(100, 200, 300)
print()
x.peek()

# popping multiple values
x.pops(5)
print()
x.peek()

# deleting stack
print()
x.__del__()


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