order = int(input('Please input the order of the square: '))
top_left = int(input('Please input the top left of the square: '))

while top_left >= order:
  print('The top left number must be between 1 and the first number entered.')
  top_left = int(input('Input the top left of the square: '))

def run(order,top_left):
  row = []
  for i in range(order):
    for i in range(order + 1):
      if top_left <= order:
        row.append(top_left)
        top_left += 1
      else:
        top_left = 1
    top_left += 1

  square = [str(x) for x in row]

  print('This is your Latin Square:\n')
  n=0
  for i in range(order):
    finish=''
    for x in range(order):
      finish += (square[n] +'  ')
      n+=1
    print(finish)

run(order, top_left)


