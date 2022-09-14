rod = int(input("Input number of rods: "))

print("")
print("Conversions list:")

def meters(rod):
    meter = rod * 5.0292
    return meter
print("Meters: ", meters(1))

def furlong(rod):
    fur = rod /40
    return fur
print("Furlongs: ", furlong(1))

def miles(rod):
    mile = meters(rod)/160.934
    return mile
print("Miles: ", miles(1))

def foot(rod):
    feet = meters(rod)/0.3048
    return feet
print("Feet: ", foot(1))

def average(rod):
    avg = ((miles(rod) /3.1)*60)
    return avg
print ("Minutes to walk ",float(rod),"rods: ", average(1))
