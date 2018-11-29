def fizzBuzz(low, high):
    print(str(low) + ' ', end="")
    if(low%3 == 0): print('fizz', end="")
    if(low%5 == 0): print('buzz', end="")
    print()
    if(low < high): fizzBuzz(low+1, high)

    return

lowInt = int(input('Enter lower bound: '))
highInt = int(input('Enter upper bount: '))
fizzBuzz(lowInt, highInt)
