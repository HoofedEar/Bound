import importlib
import sys
import glob
import math
import random
from os.path import join,basename,splitext

VERSION = "v0.2.1"
numlist = "0123456789"

def main(c):
	c = c.replace(" ", "")
	source = [char for char in c]
	source = list(reversed(source))
	length = len(source)
	var = ''
	stack = []

	while length != 0:
		try:
			current = source.pop()
		except IndexError:
			break

		if current == '.': # Output stack
			print(stack)

		if current == '+': # Addition
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(b + a)
					except TypeError:
						continue

		if current == '-': # Subtraction
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(b - a)
					except TypeError:
						continue

		if current == '*': # Multiplication
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(b * a)
					except TypeError:
						continue
				if isinstance(stack[-1], str) and isinstance(stack[-2], int):
					try:
						a = stack.pop() # the str
						b = stack.pop() # the int
						stack.append(b * a)
					except TypeError:
						continue

		if current == '%': # Modulo
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(b % a)
					except TypeError:
						continue

		if current == '/': # Divide, round up
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(math.ceil(b / a))
					except TypeError:
						continue
					except ZeroDivisionError:
						continue

		if current == '\\': # Divide, round down
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int): 
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(math.floor(b / a))
					except TypeError:
						continue
					except ZeroDivisionError:
						continue

		if current == '^': # Power
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(b ** a)
					except TypeError:
						continue

		if current == '#': # Square
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					try:
						a = stack.pop()
						stack.append(a ** 2)
					except TypeError:
						continue

		if current == '>': # Greater than
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						if (b > a):
							stack.append(1)
						else:
							stack.append(0)
					except TypeError:
						continue

		if current == '<': # Less than
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						if (b < a):
							stack.append(1)
						else:
							stack.append(0)
					except TypeError:
						continue

		if current == '=': # Integer Comparison
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						if (b == a):
							stack.append(1)
						else:
							stack.append(0)
					except TypeError:
						continue

		if current == '|': # Absolute value
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					try:
						a = stack.pop()
						stack.append(abs(a))
					except TypeError:
						continue

		if current == '!': # Factorial
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					try:
						a = stack.pop()
						stack.append(math.factorial(a))
					except TypeError:
						continue

		if current == 'g': # Pop and save in var
			if len(stack) >= 1:
				var = stack.pop()

		if current == 'G': # Replace top value with var and clear
			if len(stack) >= 1:
				if var != '':
					stack.pop()
					stack.append(var)
					var = ''

		if current == ';': # Swap top two elements
			if len(stack) >= 2:
				a = stack[-1]
				b = stack[-2]
				stack[-1] = b
				stack[-2] = a

		if current == ',': # Remove all but top
			if len(stack) >= 2:
				stack = list(map(int, str(stack[-1])))

		if current == '@': # Reverse stack
			if len(stack) >= 2:
					stack = list(reversed(stack))

		if current == '$': # sort the stack
			if len(stack) >= 2:
					stack = list(sorted(stack))

		if current == 'd': # turn the top integer into a char
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					stack.append(chr(stack.pop()))

		if current == '\'': # Top char is converted to int
			if len(stack) >= 1:
				if isinstance(stack[-1], str):
					a = stack.pop()
					stack.append(ord(a))

		if current == 's': # Write out each char in the stack
			if len(stack) >= 1:
				if isinstance(stack[-1], str):
					sys.stdout.write(stack[-1])
		
		if current == 'S': # Prints out the top string
			if len(stack) >= 1:
				if isinstance(stack[-1], str):
					print(stack[-1])

		if current == '{': # Rotate top element to the left
			if len(stack) >= 1:
				stack = stack[1:] + stack[:1]

		if current == '}': # Rotate top element to the right
			if len(stack) >= 1:
				stack = stack[-1:] + stack[:-1]

		if current == 'U': # Remove all falsy elements
			if len(stack) >= 1:
				stack[:] = [x for x in stack if x != 0]

		if current == 'R': # Repeat the next command equal to the top value 
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					for _ in list(range(a - 1)):
						try:
							source.append(source[-1])
							length = len(source)
						except IndexError:
							continue


		if current == ':': # Combines the top two elements if they are integers
			if len(stack) >= 2:
				if isinstance(stack[-1], int) and isinstance(stack[-2], int):
					try:
						a = stack.pop()
						b = stack.pop()
						stack.append(int(str(b) + str(a)))
					except TypeError:
						continue

		if current == 'c': # Put a copy of the top element
			if len(stack) >= 1:
				stack.append(stack[-1])

		if current == '&': # Puts elements from 1 to n, exclusively (expANDs)
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					exp = range(1, a+1)
					for i in list(exp):
						stack.append(i)

		if current == '~': # Randomize the stack lol
			if len(stack) >= 2:
				random.shuffle(stack)

		if current == 'n': # Puts the sum of all ints on the stack
			if len(stack) >= 1:
				total = 0
				for i in stack:
					if isinstance(i, int):
						total += i
				stack = [x for x in stack if not isinstance(x, int)]
				stack.append(total)

		if current == 'I': # Increment the top of the stack 
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					stack.append(a + 1)

		if current == 'D': # Decrement the top of the stack 
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					stack.append(a - 1)
			
		if current == '?': # Check if the top of the stack is even
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					if (a % 2 == 0):
						stack.append(1)
					else:
						stack.append(0)

		if current == 'b': # Breaks apart the top int into seprate integers
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					for i in list(map(int, str(a))):
						stack.append(i)

		if current == '(': # Loop until )
			if len(stack) >= 1:
				if isinstance(stack[-1], int):
					a = stack.pop()
					track = True
					group = ''
					offset = 0
					for i in list(reversed(source)):
						if track:
							if i != ')':
								group += i
								offset += 1
							else:
								track = False

					for i in list(range(0, offset)):
						source.pop()
					source += reversed(group * a)
					length = len(source)



		if current == 'i': # Gets input of an integer
			a = input()
			try:
				stack.append(int(a))
			except ValueError:
				continue

		if current in numlist:
			stack.append(int(current))

	print()
	print(stack)


if __name__ == "__main__":
	print("=Bound %s=" % VERSION)
	if len(sys.argv) == 1:
		while True:
			print()
			code = input("β ")
			if code == "exit":
				break
			if code == "":
				print("Hello, world!")
			else:
				main(code)
	else:
		code = sys.argv[1]
		main(code)