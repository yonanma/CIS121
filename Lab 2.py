humanage = float(input("enter your age: ")) #user imput
dogage = (7 * humanage) 
years = (dogage // 1) #the quotient for the year
month = (dogage % 1) # the remainder from the year is the month
month = (month * 12) # 1 year has 12 months so we multiply by 12
month = (month // 1) # we only take the quotient
days = (month % 1) # the remainder from the month is the days
days = (days * 30) # 1 month has 30 days so multiply with 30
days = (days // 1) # I only took the quotient
print("Your age in dog years is",(years),"years",(month),"months",(days),"days")

catage = (humanage / 9)
years = (catage // 1)  #the quotient for the year
month = (catage % 1) # the remainder from the year is the month
month = (month * 12) # 1 year has 12 months so we multiply by 12
month = (month // 1) # we only take the quotient
days = (month % 1) # the remainder from the month is the days
days = (days * 30) # 1 month has 30 days so multiply with 30
days = (days // 1) # I only took the quotient
print("Your age in cat years is",years,"years",(month),"months",(days),"days")

horseage = 3*(((((humanage)**2)- 47)/7)+12) #Formula to calculate horse age
years = (horseage // 1) #the quotient for the year
month = (horseage % 1) # the remainder from the year is the month
month = (month * 12) # 1 year has 12 months so we multiply by 12
month = (month // 1) # we only take the quotient
days = (horseage % 1) # the remainder from the month is the days
days = (days * 30) # 1 month has 30 days so multiply with 30
days = (days // 1) # I only took the quotient
print("Your age in horse years is",years,"years",month,"months",days,"days")