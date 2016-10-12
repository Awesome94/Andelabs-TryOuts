def factorial(number):  # Created a Function called factorial with the number argument
    # type: (object) -> object
    if number == 0:
        return 1  # if the number is equal to 0 the program should return one but if its more then it...
    else:  # should return the factorial of that given number
        return number * factorial(number - 1)
