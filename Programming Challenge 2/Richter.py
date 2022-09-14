richt = float(input("Enter richter scale measurement: "))

energy = 10**((1.5*richt)+4.8)
tnt = energy / 4.184*(10**9)
def richter(richt,energy,tnt):
    print("Richter value: ",richt)
    print("Equivalence in Joules: ",energy)
    print("Equivalence in tons of TNT: ",tnt)
richter()
