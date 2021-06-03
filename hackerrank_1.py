'''Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

user_action =  input ("enter a number between 1 and 100")
possible_number = int(user_action)

if possible_number <1:
        print("too small read the instructions")
elif possible_number > 100:
        print ("too big read the instructions")
else:
    if possible_number%2 != 0:
        print ("Weird")
    elif possible_number%2 == 0 and 2<= possible_number <=5:
        print ("Not Weird")
    elif possible_number%2 == 0 and 6<= possible_number <=20:
        print ("Weird")
    elif possible_number%2 == 0 and possible_number > 20:
        print ("Not Weird")