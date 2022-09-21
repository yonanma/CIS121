
"""i = 1
while i <= 10:
	print(i)
	i+=1
	
print("done with loop")"""

"""ic= float(input("How much do you make?"))

if ic < 4500000:
	print("you got this")
else:
	print("Damn you rich")"""
"""
secret_number = 4
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not (out_of_guesses):
	if guess_count < guess_limit:
		guess = input("enter a number:")
		guess_count += 1
	else: 
		out_of_guesses = True
if out_of_guesses:
	print("You Lose")
else:
	print("yayy")"""

"""secret_number = 25
guess_limit = 3
guess_count=0
guess =""
while guess != secret_number:
	if guess_count < guess_limit:
		guess = input("enter a number:")
		guess_count =+ 1
	else:
		print("you lose")"""



"""
x=int(input("enter a number:"))
if 35 <= x <= 1000:
	if x >=100:
		print(100)
	else:
		while x <= 100:
			if x % 2 == 0:
				print(x)
			x += 1"""
"""	
number= ""

while number != 0:
	number= int(input("enter a number:"))
	if number % 2 == 0:
		print("even")
	elif number % 2 == 1:
		print("odd")"""
"""
name= (input("Enter your name:"))
ic= int(input("enter your Income"))
print("hey",name,"you make",ic,"a year")
print("this is home much u make a 20 years")
money=0
done=False
years = 1
while done != True:
	if money >=10000:
		done= True
	else:
		money=ic*years
		print(money,"year",years)
		years +=1"""


name = "Yonan"
print(name[0:6])


	


