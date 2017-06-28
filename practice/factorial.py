def FirstFactorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i

    # code goes here
    return factorial


# keep this function call here
print FirstFactorial(5)

def SimpleAdding(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i

    # code goes here
    return sum


# keep this function call here
print SimpleAdding(int(raw_input('Enter the number:')))