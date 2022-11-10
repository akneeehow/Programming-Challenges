import csv
def read_csv(csv_file):
  csv_contents = []
  with open(csv_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)              
    for row in reader:
      csv_contents.append(row)
  return csv_contents

def addtotal(date, content, dict):
  totalv = 0.0
  totals = 0.0
  for x in content:
    if x[0].split('-')[:2] == date:   
      totalv += float(x[6])
      totals += float(x[5]) * float(x[6])
  dict['-'.join(date)] = [totals,totalv, (totals/totalv)]
      

def alldates(content):
  return [list(x) for x in list(set([tuple(x[0].split('-')[:2]) for x in content]))]


if __name__ == '__main__':
  contents = read_csv('AAPL.csv')
  dates = alldates(contents)
  
  volumes = {}
  for x in dates:
    addtotal(x, contents,volumes)
    
  vol2 = sorted(volumes.items(), key=lambda e: e[1][2])[::-1]
  topsix = vol2[:6]
  bottomsix = vol2[-6:][::-1]


  print('\nTOP 6\n')
  for x in topsix:
    print(f'{x[0]:<7} - {x[1]}')

  print('\nBOTTOM 6\n')
  for x in bottomsix:
    print(f'{x[0]:<7} - {x[1]}')