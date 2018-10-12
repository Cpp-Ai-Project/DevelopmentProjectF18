def checkMultiplies(r1, r2, n1, n2):
    firstMultiple = (r2-r1)/n1 + 1
    firstMultiple = int(firstMultiple)
    secondMultiple = (r2-r1)/n2 + 1
    secondMultiple = int(secondMultiple)
    bothMultiple = (r2-r1)/(n1*n2) + 1
    bothMultiple = int(bothMultiple)

    for i in range(0, firstMultiple-bothMultiple):
        print("Fizz")
    for i in range(0, secondMultiple-bothMultiple):
        print("Buzz")
    for i in range(0, bothMultiple):
        print("FizzBuzz")

def main():
    r1 = input("Enter the Start: ")
    r1 = int(r1)
    r2 = input("Enter the End: ")
    r2 = int(r2)
    n1 = input("Enter first number: ")
    n1 = int(n1)
    n2 = input("Enter second number: ")
    n2 = int(n2)
    checkMultiplies(r1, r2, n1, n2)

main()