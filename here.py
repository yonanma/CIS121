
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

"""secret_number = 4
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

secret_number = 25
guess_limit = 3
guess_count=0
guess =""
while guess != secret_number:
	if guess_count < guess_limit:
		guess = input("enter a number:")
		guess_count =+ 1
	else:
		print("you lose")
