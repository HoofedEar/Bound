import importlib
import sys
import glob
import math
from os.path import join,basename,splitext

numlist = "0123456789"

def main(c):
	source = [char for char in c]
	source = list(reversed(source))
	length = len(source)
	var = ''
	convert = False
	stack = []

	for _ in range(length):
		current = source.pop()
		print("> " + current)

		if convert == False:

			if current == 'i': # Get Input
				v = input()
				stack.append(v)

			if current == '.': # Debug, output stack
				print(stack)

			if current == '+': # Addition
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(b + a)
						except TypeError:
							continue

			if current == '-': # Subtraction
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(b - a)
						except TypeError:
							continue

			if current == '*': # Multiplication
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(b * a)
						except TypeError:
							continue

			if current == '%': # Modulo
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(b % a)
						except TypeError:
							continue

			if current == '/': # Divide, round up
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(math.ceil(b / a))
						except TypeError:
							continue

			if current == '\\': # Divide, round down
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int: 
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(math.floor(b / a))
						except TypeError:
							continue

			if current == '^': # Power
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
						try:
							a = stack.pop()
							b = stack.pop()
							stack.append(b ** a)
						except TypeError:
							continue

			if current == '#': # Square
				if len(stack) >= 1:
					if type(stack[-1]) is int:
						try:
							a = stack.pop()
							stack.append(a ** 2)
						except TypeError:
							continue

			if current == '>': # Greater than
				if len(stack) >= 2:
					if type(stack[-1]) is int and type(stack[-2]) is int:
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
					if type(stack[-1]) is int and type(stack[-2]) is int:
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
					if type(stack[-1]) is int and type(stack[-2]) is int:
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
					if type(stack[-1]) is int:
						try:
							a = stack.pop()
							stack.append(abs(a))
						except TypeError:
							continue

			if current == '!': # Factorial
				if len(stack) >= 1:
					if type(stack[-1]) is int:
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

			if current == ';': # Swap
				if len(stack) >= 2:
					a = stack[-1]
					b = stack[-2]
					stack[-1] = b
					stack[-2] = a

			if current == ',': # Remove all but top
				if len(stack) >= 2:
					stack = list(map(int, str(stack[-1])))

			if current == 'l': # Len of string
				if len(stack) >= 1:
					if type(stack[-1]) is str:
						stack[-1] = len(stack[-1])

			if current == '@': # Reverse stack
				if len(stack) >= 1:
						stack = list(reversed(stack))

			if current == '$': # sort the stack
				if len(stack) >= 1:
						stack = list(sorted(stack))

			if current == 'd': # turn the top integer into a char
				if len(stack) >= 1:
					try:
						stack.append(chr(stack.pop()))
					except ValueError:
						continue
					except OverflowError:
						continue

			if current == '\'': # Next char is converted to int
				convert = True

			if current == 's': # Write out each char in the stack
				if len(stack) >= 1:
					for x in stack:
						if type(x) is str:
							sys.stdout.write(x)

			if current == '{': # Rotate top element to the left
				if len(stack) >= 1:
					stack = stack[1:] + stack[:1]

			if current == '}': # Rotate top element to the right
				if len(stack) >= 1:
					stack = stack[-1:] + stack[:-1]

			if current == 'U': # Remove all falsy elements
				if len(stack) >= 1:
					stack[:] = [x for x in stack if x != 0]

			if current in numlist:
				stack.append(int(current))

		else:
			stack.append(ord(current))
			convert = False




if __name__ == "__main__":
	code = input("> ")
	main(code)