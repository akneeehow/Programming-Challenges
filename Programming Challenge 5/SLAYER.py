def run(layers,answer):
  if int(answer) == int(layers):
    print(f'Your guess is correct.\nSLAYER + SLAYER + SLAYER = {answer}\nLAYERS = {layers}')
  else:
    print(f'Your guess in incorrect.\nSLAYER + SLAYER + SLAYER = {answer}\nLAYERS = {layers}')
  print('Thanks for playing')



if __name__ == "__main__":
  print('Guess a six-digit number SLAYER so that following equation is true, where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS')

  guess = int(input('Enter your guess for SLAYER: '))
  
  while len(str(guess)) != 6:
    guess = int(input('Enter your guess for SLAYER: '))
  answer = guess*3
  
  guess2 = str(guess)
  
  layers = guess2[1:] + guess2[0]

  run(layers,answer)
