#factorial
#n = int(input("Enter a number : "))
def factorial(n):
    i = 1
    result = 1
    while i<=n:
        result = result*i
        i = i+1
    return result

#sum of digits
#n = int(input("Enter a digit to perform a sum opeartion :"))
def sum_digits(n):
    sum = 0
    while n>0:
        last_digit = n%10
        sum = sum + last_digit
        n = n//10
    return sum