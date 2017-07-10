sum = 0

def add(a,b):
	return(a+b)

def subtract(a,b):
	return(a-b)

def multiply(a,b):
	return(a*b)

def divide(a,b):
	return(a/b)

options= {"+": add, "-":subtract, "*":multiply, "/":divide}

def main():
	num_1 = eval(input("Number:\n"))
	operator = input("Operator:\n")
	num_2 = eval(input("Number:\n"))

	while operator != "=":
		operation = options[operator](num_1,num_2)
		num_1= sum + operation
		operator = input("Operator:\n")
		if operator != "=":
			num_2 = eval(input("Number:\n"))
		else:
			print(num_1)

main()
