# This task shows how you are able  to use a For Loop only once within a if and else statement.
 
n = 5 # number of rows
stars = 0 # number of stars in each row
for i in range(1, n * 2): # loop from 1 to n * 2
    if i <= n: # if i is less than or equal to n
        stars += 1 # increase the number of stars by 1
    else: # otherwise
        stars -= 1 # decrease the number of stars by 1
    print("*" * stars) # print the stars