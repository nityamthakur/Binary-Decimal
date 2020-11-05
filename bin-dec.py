binary=list(input("Input a binary number: "))
decimal=0
for i in range(len(binary)):
	digit=binary.pop()
	if digit == '1':
		decimal=decimal+2**i
print("The decimal value of the number is",decimal)
