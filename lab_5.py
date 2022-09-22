"""
Yonan Abraha

Lab 5
"""



def main():
	
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))





#Your code goes here.
def DecodeWord(encodword): #creating a function
  decodedWord = "" # needed a variable to exist for the next line of codes
  for i in encodword: # checking each letter in the encodedword
    if i=="L": # if the letter is "L"
      decodedWord += "T" # REPLACE IT WITH "T"
    elif i=="T": # if the letter is "T"
      decodedWord += "L"# REPLACE IT WITH "L"
    elif i=="8": #if the letter is "8"
      decodedWord += "A"# REPLACE IT WITH "A"
    elif i=="B": #if the letter is "B"
      decodedWord += "A"# REPLACE IT WITH "A"
    elif i=="A":#if the letter is "A"
      decodedWord += "E"# REPLACE IT WITH "E"
    elif i=="E":#if the letter is "E"
      decodedWord += "B"# REPLACE IT WITH "B"
    else:
      decodedWord += i
  return decodedWord

	











#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()