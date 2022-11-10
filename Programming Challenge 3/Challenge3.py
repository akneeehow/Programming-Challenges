def minusnine(x):
    return 99 - x

def result(i,j):
    return j - (int(str(i + j)[1::]) + int(str(i + j)[0]))

if __name__ == '__main__':
    num = int(input('First Player:\nEnter a number between 10 and 49: '))
    while num < 10 or num > 49:
        num = int(input('Enter a number between 10 and 49: '))
    factor = minusnine (num)

    num2 = int(input('\nSecond Player:\nEnter a number between 50 and 99: '))
    while num2 < 50 or num2 > 99:
        num2 = int(input('Enter a number between 50 and 99: '))
  
    print(f'\nI said the answer was {num} and the calculation result is {result(factor,num2)}')