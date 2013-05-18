
#http://content.codersdojo.org/code-kata-catalogue/roman-numerals/

def convertToRomanNumeral(number):
	RomanNumerals = ["I", "V", "X", "L", "D", "M"]
	romanNumeral = ""
	currentNumber = number
	while currentNumber > 0:
		if currentNumber >= 1000:
			romanNumeral += "M"
			currentNumber -= 1000
		elif currentNumber >= 500:
			romanNumeral += "D"
			currentNumber -= 500
		elif currentNumber >= 50:
			romanNumeral += "L"
			currentNumber -= 50
		elif currentNumber >= 10:
			romanNumeral += "X"
			currentNumber -= 10
		elif currentNumber >= 5:
			romanNumeral += "V"
			currentNumber -= 5
		elif currentNumber >= 1:
			romanNumeral += "I"
			currentNumber -= 1
		
	return romanNumeral

#testing
i = 0
while i < 100:
	i += 1
	print convertToRomanNumeral(i)



