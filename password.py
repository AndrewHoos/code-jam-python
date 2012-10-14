

#written by Andrew Hoos
# andrewhoos.com

import sys
import re


def expectation(total, typed, deleted=0, enter=False):
  if(enter):
    return total+2
  prob_correct = values[typed-deleted-1]
  outcome_correct = total + 2*deleted + 1 - typed
  prob_incorrect = 1 - prob_correct
  outcome_incorrect = 2*total + 2*deleted+2-typed
   
  return prob_correct*outcome_correct +prob_incorrect*outcome_incorrect
  

number_of_cases = int(sys.stdin.readline().strip())

for case in range(number_of_cases):

  line = sys.stdin.readline().strip()

  typed = int(line.split()[0])
  total = int(line.split()[1])
  
  #read the percentages
  values = sys.stdin.readline().strip().split()
  
  #convert to numbers
  for i in range(len(values)):
    values[i] = float(values[i])
  
  #calculated acumulated probablity
  for i in range(1, len(values)):
    values[i]=values[i]*values[i-1]

  minimum = expectation(total,typed,enter=True)

  for delete in range(typed):
    exp = expectation(total,typed,delete)
    if exp < minimum:
      minimum = exp
  
  print("Case #"+str(case+1),end="")
  print(": %0.6f" % minimum)


  
