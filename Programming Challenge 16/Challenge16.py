def management(debt, interest, repay):
  total = 0
  months = 0
  while debt > 0:
    debt += round(debt * interest,2)
    
    if debt < 50:
      total += debt
      months +=1
      break
    if debt * repay > 50:
      total += round(debt * repay,2)
      debt -= round(debt * repay,2)
      months += 1
    else:
      debt -= 50
      total += 50
      months +=1
    interest = round(debt / 1000,2)

  print("\n\nTotal amount repaid: £",round(total,2))
  print(f'It took {months} months to pay off this debt')

if __name__ == "__main__":
  debt = int(input("Enter intial debt: "))
  interest = int(input("Enter interest rate: "))/100
  repay = int(input("Enter repayment rate: "))/100
  management(debt, interest, repay)