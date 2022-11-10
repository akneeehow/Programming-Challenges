def shift(shift, word):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  ring = alphabet
  newword = ''
  for x in word:
    newring = ring[shift:] + ring[:shift]
    newword += newring[alphabet.index(x)]
    ring = newring[1:]+newring[:1]
  return newword

if __name__ == '__main__':
  plain = input('Enter word to encrypt: ')
  shifts = int(input('Enter shift: '))
  print(f"Encrypted Word: {shift(shifts-1, plain)}")