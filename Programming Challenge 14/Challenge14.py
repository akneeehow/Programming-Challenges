def calculator(str):
  if str[2] == "+":
    return int(int(str[0])+int(str[1]))
  elif str[2] == "-":
    return int(int(str[0])-int(str[1]))
  elif str[2] == "*":
    return int(int(str[0])*int(str[1]))
  elif str[2] == "/":
    return int(int(str[0])/int(str[1]))
  elif str[2] == "//":
    return int(int(str[0])//int(str[1]))
  elif str[2] == "%":
    return int(int(str[0])%int(str[1]))
  elif str[2] == "**":
    return int(int(str[0])**int(str[1]))


if __name__ == "__main__":
  calc = input("Enter your calculation: ").split(" ")
  while calc != ['q']:
    print(calculator(calc))
    calc = input('Enter your calculation: ').split(' ')
  quit()
