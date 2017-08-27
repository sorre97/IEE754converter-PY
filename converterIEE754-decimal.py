# -*- coding: utf-8 -*-

from math import fsum

binum = "00111111001100110011001100110011"


#Functions
def valid_cheker(binary):
	if not len(binary) == 32: return False
	for i in binum:
		if i != "0" and i != "1": return False
	return True

def binary_conversion(SIGN,EXP,MAN):
	SIGN = -1 if SIGN == "1" else  1
	EXP = int(EXP,2) - 127
	MAN = [1,binary_man_unpacker(MAN)]
	MAN = fsum(MAN)
	number = SIGN * MAN * (2 ** EXP)

	return number

def binary_man_unpacker(MAN):
	total = 0
	for i in range(0,len(MAN)):
		if MAN[i] == "1":
			total += (2 ** -(i+1))
	return total
		

#Code
print ("Hi, this is a converter for IEE754 binary numbers to decimals for single precision only (FLOAT)")
print "Please insert your binary code above"


while (True):
	binum = raw_input(": ")
	if not valid_cheker(binum) == True: 
		print "Error, the number inserted is not valid, please insert it again"
	else:
		break

if int(binum,2) == 0:
	print "The value is conventionally 0"
else:

	SIGN = binum[0]
	EXP = binum[1:9]
	MAN = binum[9:]

	#DISTINGUERE I CASI INFINITO,NUMERO DENORMALIZZATO ETC...
	
	number = binary_conversion(SIGN,EXP,MAN)
	rounded_number = round(number,3)
	print str(number) + " ≈ " + str(rounded_number)
	
