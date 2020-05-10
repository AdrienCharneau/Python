#!/usr/bin/python3.8
# -*-coding:Utf-8 -*
#
print("Indiquez une année:")
userInput = input()
#
if userInput.isnumeric() is not True:
	print("Ceci n'est pas une année")
else:
	userInput = int(userInput)
#
	if userInput % 4 == 0 and userInput % 100 == 0 and userInput % 400 == 0:
		print("Ceci est bien une année bissextile")
	else:
		print("Ceci n'est pas une année bissextile")