# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
is_even = False
def even_or_odd(num):
    if num%2==0:
        is_even = True
    else:
        is_even = False
    return is_even
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if even_or_odd(num):
    print('Even!')
else:
    print('Odd')
