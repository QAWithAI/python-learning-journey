#In this lab you will practice the basics of Python by building a small 
# app that creates a number pattern.
#Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
def number_pattern(n):
    # Validate: must be integer
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    # Validate: must be greater than 0
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    # Build the pattern using a for loop
    result = ''
    for i in range(1, n + 1):
        if i == 1:
            result += str(i)
        else:
            result += ' ' + str(i)
    return result
