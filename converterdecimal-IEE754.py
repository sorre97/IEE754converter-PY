# -*- coding: utf-8 -*-
from math import modf
#TEST = #22 #0.754 #-22.5
#Functions
def decToBin(decimal):
	binary = ""
	for i in range(31):
		if (decimal * 2) >= 1:
			binary += "1"
			decimal = (decimal * 2) - 1
		else:
			binary += "0"
			decimal *= 2
	return binary



def normalizer(binum):
	""" This function returns a list of two elements.
		the first one is the normalized number, and the second is the exponent value """
	string = ""
	exp = 1
	if binum[0] == "0":
		for i in range(0,len(binum)):
			exp -= 1
			if binum[i+1] == "1":
				string = "1." + binum[i+2:]
				break
	else:
		exp = binum.index(".") -1
		string = "1." + binum[1:].replace(".","")

	exp = bin(exp + 127)[2:].zfill(8)
	return [string,exp]
		

#Code
print ("Hi, this is a converter for decimals numbers to IEE754 binary for single precision only (FLOAT)")
print "Please insert your decimal value above"


while (True):
	
	try:
		num = raw_input(": ")
		num = float(num)
		break;
	except ValueError:
		print "The value inserted is not valid, please insert it again"


SIGN = "0" if num > 0 else "1"
num = abs(num)
decimal,integer = modf(num)

integerbin = bin(int(integer))[2:] #Integer value
decimalbin = decToBin(decimal)	#Decimal value
binaryNum = integerbin + "." + decimalbin #Concatenation of integer + decimal
MAN,EXP = normalizer(binaryNum) #Normalizing number point
MAN = MAN[2:25]

IEE754 = (SIGN + EXP + MAN)
print IEE754
print "Sign: ",SIGN
print "Exponent: ",EXP
print "Mantissa: ",MAN
