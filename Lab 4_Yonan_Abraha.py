upper_b_number= int(input("Enter an upper bound number:"))#input

abundant_count = 0#variable
perfect_count = 0#variable
deficient_count = 0#variable
divisor_sum = 0 #variable

for i in range(1, upper_b_number+1): # i is the range between 1, the upper b number 
  for x in range (1, i):# x is the range between 1,i 
    if i % x== 0:# i did this to know the divisor 
      divisor_sum += x # to add the divsor sum
  if(divisor_sum >i):# if divisor sum is less than i it is an abundant number 
    abundant_count += 1# so we add 1
  elif (divisor_sum < i):# if sum is less than i that makes it deficient
    deficient_count += 1# so add 1
  elif (divisor_sum ==i):#if the sum is equal to the number then it is perfect
    perfect_count += 1# add one if the code above works
  
  divisor_sum = 0# to reset the sum
  
print("Between 1 and",upper_b_number, "there are" , deficient_count,"deficient numbers",perfect_count,"perfect numbers ",abundant_count,"abundant numbers ")
