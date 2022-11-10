card = input('What is your card number: ')

def alphabet(card):
  contains = False
  for x in card:
    if x.isalpha():
      contains = True
  return contains    

def cardlen(card):
  while alphabet(card):
    print('Card number must be just numbers')
    card = input('Enter card number: ')
  while len(card) < 16:
    print('Too Short')
    card = input('Enter card number: ')
  while len(card) > 16:
    print('Too Long')
    card = input('Enter card number: ')

  return card

def digit_add(digit):
  if digit < 10:
    return digit
  else:
    return (digit % 10) + (digit // 10)

def double_list(num):
  list = []
  c = 1
  while c != len(num)+1:
    if c % 2:
      list.append(num[c-1]*2)
    else:
      list.append(num[c-1])
    c += 1
  return list
  
def luhn(num):
  checksum = int(num[-1])
  num = [int(x) for x in num[:-1]][::-1]
  doubles = double_list(num)
  doob = [digit_add(x) for x in doubles]
  return 10-(sum(doob) % 10) == checksum

def issuer(num):
  identity = ''
  if num[:2] in ['34', '37']:
    identity = 'American Express'
  elif num[:2] in ['51','52','53','54','55']:
    identity = 'Mastercard'
  elif num[0] == '4':
    identity = 'Visa'
  if num[0] == '3':
    identity = 'JCB'
  return identity

if __name__ == '__main__':

  
  cardno = input('Enter Card No: ')
  cardno = cardlen(cardno)

  if luhn(cardno):
    print(f'\nCard is valid')
    print(f'\nCard Issuer: {issuer(cardno)}\n')
  else:
    print('Card is not valid.')
