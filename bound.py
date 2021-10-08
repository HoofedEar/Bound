"""
Bound Interpreter
v0.3f
by HoofedEar
"""

import sys
import math
import random

VERSION = "v0.3"


class Interpreter:
    """
    Interpreter class
    code = code to be executed by the interpreter
    """
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

    def debug(self):
        """Debug function for debugging"""
        print(self.code)
        print(self.tape)
        print(self.current)

    def addition(self):
        """Add the top two elements of the stack"""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b + _a)
                except TypeError:
                    print("TypeError! at " + self.current)

    def subtraction(self):
        """Subtract the top element from the second top element."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b - _a)
                except TypeError:
                    print("TypeError! at " + self.current)

    def multiplication(self):
        """Multiply the top two elements together."""
        if len(self.stack) >= 2:
            try:
                _a = self.stack.pop()  # the str
                _b = self.stack.pop()  # the int
                self.stack.append(_b * _a)
            except TypeError:
                print("TypeError! at " + self.current)

    def modulo(self):
        """Modulo with the top two elements."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b % _a)
                except TypeError:
                    print("TypeError! at " + self.current)

    def divide_up(self):
        """Divide the second top element by the top element, rounded up."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(math.ceil(int(_b) / int(_a)))
                except TypeError:
                    print("TypeError! at " + self.current)
                except ZeroDivisionError:
                    print("Divided by Zero! at " + self.current)

    def divide_down(self):
        """Divide the second top element by the top element, rounded down."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(math.floor(int(_b) / int(_a)))
                except TypeError:
                    print("TypeError! at " + self.current)
                except ZeroDivisionError:
                    print("Divided by Zero! at " + self.current)

    def exponent(self):
        """Multiply the second element to the power of the top element."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b ** _a)
                except TypeError:
                    print("TypeError! at " + self.current)

    def square(self):
        """Square the top element."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(_a ** 2)
                except TypeError:
                    print("TypeError! at " + self.current)

    def greater_than(self):
        """Greater than involving the top two elements."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    if _b > _a:
                        self.stack.append(1)
                    else:
                        self.stack.append(0)
                except TypeError:
                    print("TypeError! at " + self.current)

    def less_than(self):
        """Less than involving the top two elements."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    if _b < _a:
                        self.stack.append(1)
                    else:
                        self.stack.append(0)
                except TypeError:
                    print("TypeError! at " + self.current)

    def comparison(self):
        """Integer comparison with top two elements."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    if _b == _a:
                        self.stack.append(1)
                    else:
                        self.stack.append(0)
                except TypeError:
                    print("TypeError! at " + self.current)

    def absolute_value(self):
        """Absolute value of the top most element."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(abs(_a))
                except TypeError:
                    print("TypeError! at " + self.current)

    def put_var(self):
        """Add to the top of the stack the stored element, if it exists."""
        if len(self.stack) >= 1:
            if self.stack_var != '':
                self.stack.append(self.stack_var)
                self.stack_var = ''

    def factorial(self):
        """Factorial the top element."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(math.factorial(_a))
                except TypeError:
                    print("TypeError! at " + self.current)

    def swap(self):
        """Swap the top two elements."""
        if len(self.stack) >= 2:
            _a = self.stack[-1]
            _b = self.stack[-2]
            self.stack[-1] = _b
            self.stack[-2] = _a

    def isolate(self):
        """Remove all but the top element."""
        if len(self.stack) >= 2:
            self.stack = [self.stack[-1]]

    def reverse(self):
        """Reverses the stack."""
        if len(self.stack) >= 2:
            self.stack = list(reversed(self.stack))

    def capture(self):
        """Add to the top of the stack the stored element, if it exists."""
        if len(self.stack) >= 1:
            self.stack_var = self.stack.pop()

    def sort(self):
        """Sort the stack."""
        if len(self.stack) >= 2:
            self.stack = list(sorted(self.stack))

    def to_char(self):
        """Convert the top integer into a char."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                self.stack.append(chr(self.stack.pop()))

    def to_int(self):
        """The top element is converted into an integer, if char."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                _a = self.stack.pop()
                self.stack.append(ord(_a))

    def write(self):
        """Writes out the top element in the stack to stdout."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                sys.stdout.write(self.stack[-1])
            else:
                sys.stdout.write(str(self.stack[-1]))

    def print(self):
        """Writes out the top element in the stack to stdout, with newline."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                print(self.stack[-1])
            else:
                print(str(self.stack[-1]))

    def wrap_left(self):
        """Rotates the top element to the left."""
        if len(self.stack) >= 1:
            self.stack = self.stack[1:] + self.stack[:1]

    def wrap_right(self):
        """Rotates the top element to the right."""
        if len(self.stack) >= 1:
            self.stack = self.stack[-1:] + self.stack[:-1]

    def expel_false(self):
        """Removes all falsey elements from the stack."""
        if len(self.stack) >= 1:
            self.stack[:] = [x for x in self.stack if x != 0]

    def repeat(self):
        """Repeats the next command n times, where n is top value."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                for _ in list(range(_a - 1)):
                    try:
                        self.tape.append(self.tape[-1])
                        self.tape_length = len(self.tape)
                    except IndexError:
                        print("IndexError! at " + self.current)

    def combine(self):
        """Combines the top two values into one if they are both ints."""
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(int(str(_b) + str(_a)))
                except TypeError:
                    print("TypeError! at " + self.current)

    def copy(self):
        """Puts a copy of the top element onto the stack."""
        if len(self.stack) >= 1:
            self.stack.append(self.stack[-1])

    def expand(self):
        """Puts elements 1 to n onto the stack, exclusively."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                _exp = range(1, _a + 1)
                for i in list(_exp):
                    self.stack.append(i)

    def randomize(self):
        """Randomizes the stack."""
        if len(self.stack) >= 2:
            random.shuffle(self.stack)

    def sum_all(self):
        """Sums all ints in the stack together."""
        if len(self.stack) >= 1:
            _total = 0
            for i in self.stack:
                if isinstance(i, int):
                    _total += i
            self.stack = [x for x in self.stack if not isinstance(x, int)]
            self.stack.append(_total)

    def increment(self):
        """Increments the top element of the stack."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                self.stack.append(_a + 1)

    def decrement(self):
        """Decrements the top element of the stack."""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                self.stack.append(_a - 1)

    def break_apart(self):
        """Splits the top element into separate integers"""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                for i in list(map(int, str(abs(_a)))):
                    self.stack.append(i)

    def input(self):
        """Gets input and puts it to the stack if its an int"""
        _a = input()
        try:
            self.stack.append(int(_a))
        except ValueError:
            print("ValueError! at " + self.current)

    def length(self):
        """Puts the total number of elements onto the stack."""
        if len(self.stack) >= 1:
            self.stack.append(len(self.stack))

    def is_even(self):
        """Checks if the top element is even. (Lazy modulo)"""
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                if _a % 2 == 0:
                    self.stack.append(1)
                else:
                    self.stack.append(0)

    def start(self):
        """Executes the loaded code"""
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
                case '*':
                    self.multiplication()
                case '%':
                    self.modulo()
                case '/':
                    self.divide_up()
                case '\\':
                    self.divide_down()
                case '^':
                    self.exponent()
                case '#':
                    self.square()
                case '>':
                    self.greater_than()
                case '<':
                    self.less_than()
                case '=':
                    self.comparison()
                case '|':
                    self.absolute_value()
                case '!':
                    self.factorial()
                case 'g':
                    self.capture()
                case 'G':
                    self.put_var()
                case ';':
                    self.swap()
                case ',':
                    self.isolate()
                case '@':
                    self.reverse()
                case '$':
                    self.sort()
                case 'd':
                    self.to_char()
                case '\'':
                    self.to_int()
                case 's':
                    self.write()
                case 'S':
                    self.print()
                case '{':
                    self.wrap_left()
                case '}':
                    self.wrap_right()
                case 'U':
                    self.expel_false()
                case 'R':
                    self.repeat()
                case ':':
                    self.combine()
                case 'c':
                    self.copy()
                case '&':
                    self.expand()
                case '~':
                    self.randomize()
                case 'n':
                    self.sum_all()
                case 'I':
                    self.increment()
                case 'D':
                    self.decrement()
                case 'b':
                    self.break_apart()
                case '_':
                    self.length()
                case 'i':
                    self.input()
                case '?':
                    self.is_even()
                case ('0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'):
                    self.stack.append(int(self.current))

        print()
        if self.output:
            print(self.stack)


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
                interpreter = Interpreter(code)
                interpreter.start()
    else:
        code = sys.argv[1]
        interpreter = Interpreter(code)
        interpreter.start()


if __name__ == "__main__":
    main()
