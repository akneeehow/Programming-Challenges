def palindrome(x):
  if str(x)[::-1] == str(x):
    return True
  else:
    return False

def revadd(f):
  return f + int(str(f)[::-1])

def checklych(y):
  c = 0
  while c < 70:
    if palindrome(y):
      return True
    else:
      c += 1
      y=revadd(y)
  return False

def main(num1, num2):
	palcount = 0
	lychrel = []
	nonlych = 0
	for i in range(num1, num2+1):
		if palindrome(i):
			palcount += 1
		else:
			if checklych(revadd(i)):
				nonlych += 1
			else:
				lychrel.appnum2(i)
    
	printer(lychrel, palcount, nonlych)

def printer(lych,pal,non):
	for x in lych:
		print(f'{x} is probably lychrel')
		print(f'Palindrome numbers: {pal}\nNot Lychrel numbers: {non}\nLychrel = {len(lych)}')
      
if __name__ == '__main__':
  num = int(input('Integer 1: '))
  num2 = int(input('Integer 2: '))
  
  main(num,num2)