"""
Bound Interpreter
v0.2.4f
by HoofedEar
"""

import sys
import math
import random

VERSION = "v0.2.4f"


class Interpreter:
    def __init__(self, code):
        self.code = code
        self.code = self.code.replace(" ", "")
        self.tape = list(reversed(self.code))
        self.tape_length = len(self.tape)
        self.stack = []
        self.stack_var = ''
        self.output: bool = False
        self.number_list: str = "0123456789"
        self.current = ''

    def addition(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b + _a)
                except TypeError:
                    return 0

    def subtraction(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b - _a)
                except TypeError:
                    return 0

    def start(self):
        while self.tape_length != 0:
            try:
                self.current = self.tape.pop()
            except IndexError:
                break

        match self.current:

            case '.':
                self.output = not self.output

            case '+':
                self.addition()

            case '-':
                self.subtraction()



def main():
    """Main function that handles input"""
    print(f"=Bound {VERSION}=")
    if len(sys.argv) == 1:
        while True:
            print()
            code = input("β ")
            if code == "exit":
                break
            if code == "":
                print("Hello, world!")
            else:
                interpreter(code)
    else:
        code = sys.argv[1]
        interpreter(code)


def interpreter(c):
    """
    Bound interpreter
    c: str - string that is to be executed by the interpreter
    """
    c = c.replace(" ", "")
    tape = list(reversed(c))
    tape_length = len(tape)
    stack = []
    stack_var = ''
    output: bool = False
    number_list: str = "0123456789"

    while tape_length != 0:
        try:
            current = tape.pop()
        except IndexError:
            break

        match current:

            case '.':  # Toggle stack output at end of execution
                output = not output

            case '+':  # Addition
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(b + a)
                        except TypeError:
                            continue

            case '-':  # Subtraction
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(b - a)
                        except TypeError:
                            continue

            case '*':  # Multiplication
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            _a = stack.pop()
                            _b = stack.pop()
                            stack.append(_b * _a)
                        except TypeError:
                            continue
                    if isinstance(stack[-1], str) and isinstance(stack[-2], int):
                        try:
                            _a = stack.pop()  # the str
                            _b = stack.pop()  # the int
                            stack.append(_b * _a)
                        except TypeError:
                            continue

            case '%':  # Modulo
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(b % a)
                        except TypeError:
                            continue

            case '/':  # Divide, round up
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(math.ceil(int(b) / int(a)))
                        except TypeError:
                            continue
                        except ZeroDivisionError:
                            continue

            case '\\':  # Divide, round down
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(math.floor(int(b) / int(a)))
                        except TypeError:
                            continue
                        except ZeroDivisionError:
                            continue

            case '^':  # Power
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(b ** a)
                        except TypeError:
                            continue

            case '#':  # Square
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        try:
                            a = stack.pop()
                            stack.append(a ** 2)
                        except TypeError:
                            continue

            case '>':  # Greater than
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            if b > a:
                                stack.append(1)
                            else:
                                stack.append(0)
                        except TypeError:
                            continue

            case '<':  # Less than
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            if b < a:
                                stack.append(1)
                            else:
                                stack.append(0)
                        except TypeError:
                            continue

            case '=':  # Integer Comparison
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            if b == a:
                                stack.append(1)
                            else:
                                stack.append(0)
                        except TypeError:
                            continue

            case '|':  # Absolute value
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        try:
                            a = stack.pop()
                            stack.append(abs(a))
                        except TypeError:
                            continue

            case '!':  # Factorial
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        try:
                            a = stack.pop()
                            stack.append(math.factorial(a))
                        except TypeError:
                            continue

            case 'g':  # Pop and save in stack_var
                if len(stack) >= 1:
                    stack_var = stack.pop()

            case 'G':  # Replace top value with stack_var and clear
                if len(stack) >= 1:
                    if stack_var != '':
                        stack.pop()
                        stack.append(stack_var)
                        stack_var = ''

            case ';':  # Swap top two elements
                if len(stack) >= 2:
                    a = stack[-1]
                    b = stack[-2]
                    stack[-1] = b
                    stack[-2] = a

            case ',':  # Remove all but top
                if len(stack) >= 2:
                    stack = [stack[-1]]

            case '@':  # Reverse stack
                if len(stack) >= 2:
                    stack = list(reversed(stack))

            case '$':  # sort the stack
                if len(stack) >= 2:
                    stack = list(sorted(stack))

            case 'd':  # turn the top integer into a char
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        stack.append(chr(stack.pop()))

            case '\'':  # Top char is converted to int
                if len(stack) >= 1:
                    if isinstance(stack[-1], str):
                        a = stack.pop()
                        stack.append(ord(a))

            case 's':  # Write out top element
                if len(stack) >= 1:
                    if isinstance(stack[-1], str):
                        sys.stdout.write(stack[-1])
                    else:
                        sys.stdout.write(str(stack[-1]))

            case 'S':  # Prints out the top element
                if len(stack) >= 1:
                    if isinstance(stack[-1], str):
                        print(stack[-1])
                    else:
                        print(str(stack[-1]))

            case '{':  # Rotate top element to the left
                if len(stack) >= 1:
                    stack = stack[1:] + stack[:1]

            case '}':  # Rotate top element to the right
                if len(stack) >= 1:
                    stack = stack[-1:] + stack[:-1]

            case 'U':  # Remove all falsy elements
                if len(stack) >= 1:
                    stack[:] = [x for x in stack if x != 0]

            case 'R':  # Repeat the next command equal to the top value
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        for _ in list(range(a - 1)):
                            try:
                                tape.append(tape[-1])
                                tape_length = len(tape)
                            except IndexError:
                                continue

            case ':':  # Combines the top two elements if they are integers
                if len(stack) >= 2:
                    if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        try:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(int(str(b) + str(a)))
                        except TypeError:
                            continue

            case 'c':  # Put a copy of the top element
                if len(stack) >= 1:
                    stack.append(stack[-1])

            case '&':  # Puts elements from 1 to n, exclusively (expANDs)
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        exp = range(1, a + 1)
                        for i in list(exp):
                            stack.append(i)

            case '~':  # Randomize the stack lol
                if len(stack) >= 2:
                    random.shuffle(stack)

            case 'n':  # Puts the sum of all ints on the stack
                if len(stack) >= 1:
                    total = 0
                    for i in stack:
                        if isinstance(i, int):
                            total += i
                    stack = [x for x in stack if not isinstance(x, int)]
                    stack.append(total)

            case 'I':  # Increment the top of the stack
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        stack.append(a + 1)

            case 'D':  # Decrement the top of the stack
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        stack.append(a - 1)

            case '?':  # Check if the top of the stack is even
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        if a % 2 == 0:
                            stack.append(1)
                        else:
                            stack.append(0)

            case 'b':  # Breaks apart the top int into separate integers
                if len(stack) >= 1:
                    if isinstance(stack[-1], int):
                        a = stack.pop()
                        for i in list(map(int, str(abs(a)))):
                            stack.append(i)

            case '_':  # Add the number of elements in the stacks to the stack
                if len(stack) >= 1:
                    stack.append(len(stack))

            case 'i':  # Gets input of an integer
                a = input()
                try:
                    stack.append(int(a))
                except ValueError:
                    continue

        if current in number_list:
            stack.append(int(current))

    print()
    if output:
        print(stack)


if __name__ == "__main__":
    main()
