# Initialize name as an empty string
name = ''

# If the user enters a blank string for name, then the while statement’s condition will be True, and the program continues to ask for a name.
while not name:
    print('Enter your name:')
    name = input()

# Ask for the number of guests
print('How many guests will you have?')
numOfGuests = int(input())

# If the value for numOfGuests is not 0, then the condition is considered to be True, and the program will print a reminder for the user.
if numOfGuests:
    print('Be sure to have enough room for all your guests.')

# End 
print('Done')

# "You could have entered not name != '' instead of not name, and numOfGuests != 0 instead of numOfGuests, but using the truthy and falsey values can make your code easier to read."
# Source: Automate the Boring Stuff
