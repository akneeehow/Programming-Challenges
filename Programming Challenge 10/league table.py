import csv

with open('Premier 16-17.csv') as csvfile:
    table = []
    c = csv.reader(csvfile,delimiter=',')
    next(c)
    for row in c:
        table.append(row)
team = 'Arsenal'
def points(team,table):
    point = 0
    for row in table:
        if row[1] == team:
            if row[3] > row[4]:
                point += 3
            if row[3] == row[4]:
                point += 1
        if row[2] == team:
            if row[3] < row[4]:
                point += 3
            if row[3] == row[4]:
                point += 1
    return (point)
print("Points = ",points(team, table))       
        
