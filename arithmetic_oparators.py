'''The provided code stub reads two integers from STDIN,  A and B. 
Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

#works on command line but not in vs code? Def not on hackerrank

user_input_1 = input("enter a number greater than 1 ")
a = int(user_input_1)
user_input_2 = input("enter a number greater than 1")
b = int(user_input_2)

sum = a + b
print(sum)

difference = a - b
print(difference)

product = a * b
print(product)
