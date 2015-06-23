#Get input from stdin and convert to int
N = int(input())

diagonals = [0,0]
  
#Set up for loop for each line in matrix
for k in range(0,N):
    #Read line
    line = input() 
    #Split into sequence based on whitespace
    row = [int(x) for x in line.split()]
    #Use consecutive integers from k =[0,N) as indecices
    diagonals[0] += row[k]
    row.reverse()
    diagonals[1] += row[k]

#Fake Absolute value
if diagonals[0] > diagonals[1]:
    difference = diagonals[0] - diagonals[1]
else:
    difference = diagonals[1] - diagonals[0]

print(difference)

