def FizzBuzz(number):
	if number % 15 == 0:
		return "FizzBuzz"
	elif number % 5 == 0:
		return "Fizz"
	elif number % 3 == 0:
		return "Buzz"
	else:
		return number


print "1:", FizzBuzz(1)
print "2:", FizzBuzz(2)
print "3:", FizzBuzz(3)
print "4:", FizzBuzz(4)
print "5:", FizzBuzz(5)
print "6:", FizzBuzz(6)
print "10:", FizzBuzz(10)
print "15:", FizzBuzz(15)





