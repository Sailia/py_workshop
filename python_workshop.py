# Variable type does not need to be declared
# Data Types: Numbers, Strings, List, Tuple, Dictionary

print('------------')

int = 3

print(int)

print('------------------------')

age = 29

if age > 10 and age < 20:
	if age % 10 == 1:
		print("Its your " + str(age) + "st birthday!")
	elif age % 10 == 2:
		print("Its your " + str(age) + "nd birthday!")
	elif age % 10 == 3:
		print("Its your " + str(age) + "rd birthday!")
else:
	print("Its your " + str(age) + "th birthday!")
print("My age is: #{age}")

"My age is " + age + "." 