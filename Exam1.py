#1 a: it does not work because it does not have a print statement
#b:it will work but it ill be stuck in an infinte loop. i would fix it by adding one each time after the print statment
#c it works
#d it will not work beacause of the indentation
#e it is never going to equal yo 5 so it can not break out of the loop and also it does not have a print satatment so it will not work
#2
"""
milk = float(input("Enter amount of milk:"))#user input
eggs = float(input("Enter amount of eggs:"))#user input
bacon =  float(input("Enter amount of eggs:")) #user input

x= (milk * 2.00 + eggs * 1.50 + bacon * 3.00) # calculating the price
tax= x * 0.11# adding the tax

print (x + tax)
"""
"""
#3
ph="6518083815" #input
print("(",ph[0:3],")",ph[3:6],"-",ph[6:10])# usiing string munipilation 
"""

#4
"""
for x in range (1,61): # this line of code helps me go through each number in the given range 
    if 48 % x == 0:# finding the 10 divisor
        if x < 15:
            x % 2==0 # checking if even
            print (x)
        elif x >= 15:
            x % 2==0 #checking if even
            print("I generated the number",x, "randomly")
"""