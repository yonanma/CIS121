"""
Yonan Abraha
08/09/22

Calculator to calculate taxs
"""
import sys


taxOwed = 0.0
tax = 0
earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




if maritalStatus == "s": # this is saying if single do the code under
  if earnedIncome <= 9950:  # if it less than 9950 
     tax= earnedIncome * (0.1) # mutiplying it with 10%
  elif earnedIncome <=40525 : # if less than 40525
     tax= ((earnedIncome - 9950) * 0.12) + (0.1 * 9950) # we substract the 9950 so it does not get taxed twice and do the same thing up top
  elif earnedIncome <= 86375: # if less than 86375
     tax= ((earnedIncome - 40526) * 0.22) + (0.12 * (40525 - 9950)) + (0.1 * 9950) # we subtract the 40526 and tax it 22% then subtract from the 40525 to do the 12% then the remaing 10%
  elif earnedIncome >= 150000:print("you made too much, Harry")
	



if maritalStatus == "m":# this is saying if married do the code under
   if earnedIncome <= 19900:# if it less than 19900
    tax= earnedIncome * 0.1 # mutiplying it with 10%
   elif earnedIncome <=81050:# if less than 81050
    tax= (earnedIncome -19900) * (0.12) + (0.1 * 19900)# im doing the same process like the one up top we are breaking it down 
   elif earnedIncome <= 172750:
    tax= (earnedIncome - 81051) * (0.22) + (0.12 * (81051-19901)) + (0.1 * 19900) 
   else:
    print("done")

print("This year you owe",tax,"in taxes") 