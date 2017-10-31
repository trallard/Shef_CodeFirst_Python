#more arguments
def add_two_numbers ():
	number1 = 1
	number2 = 3
	answer = number1 + number2
	print ("{} plus {} is {}".format (number1, number2,answer))

add_two_numbers ()
add_two_numbers ()
add_two_numbers ()

def add_two_numbers_from_arguments(number1, number2):
	answer= number1 + number2
	print ("{} plus {} is {}".format (number1, number2, answer))

add_two_numbers_from_arguments (2,5)

def add_two_numbers_and_return_value():
        number1 =1
        number2 =2
        answer = number1 + number2   # answer = 3_
        return answer   #3

returned_value = add_two_numbers_and_return_value()

print (returned_value)
