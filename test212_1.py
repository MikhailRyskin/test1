def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


my_numb = 5
my_fact = factorial(my_numb)
print(my_fact)
