def process(isbn):
  total = 0 
  c = 10
  for x in [*isbn]:
    if x == 'x':
      total += c * 10
    elif x == '?':
      multiple = c
    else:
      total += c * int(x)
    c -= 1
  
  digit = 0
  while total % 11 != 0:
    total += multiple
    digit += 1
  if digit == 10:
    digit = 'X'
  return digit

if __name__ == '__main__':
  isbn = input('Enter ISBN number: ')
  ans = process(isbn)
  print(f'Missing digit is {ans}')