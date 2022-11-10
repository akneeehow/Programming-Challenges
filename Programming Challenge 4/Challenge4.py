def chill(air_temp, air_speed):
  windchill = 35.74 + 0.6215 *air_temp - 35.75 * air_speed**0.16 + 0.4275*air_temp*air_speed**0.16
  return windchill

def run(air_temp, air_speed):
  print(f'Temperature of {air_temp} and speed of {air_speed} gives windchill of {chill(air_temp, air_speed)}\n')





if __name__ == "__main__":

  run(10, 15)
  run(0, 25)
  run(-10, 35)
  temp = float(input('Enter Temperature: '))
  speed = float(input('Enter Speed: '))
  run(temp, speed)