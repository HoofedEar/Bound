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

    def debug(self):
        print(self.code)
        print(self.tape)

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

    def multiplication(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b * _a)
                except TypeError:
                    return 0
            if isinstance(self.stack[-1], str) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()  # the str
                    _b = self.stack.pop()  # the int
                    self.stack.append(_b * _a)
                except TypeError:
                    return 0

    def modulo(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b % _a)
                except TypeError:
                    return 0

    def divide_up(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(math.ceil(int(_b) / int(_a)))
                except TypeError:
                    return 0
                except ZeroDivisionError:
                    return 0

    def divide_down(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(math.floor(int(_b) / int(_a)))
                except TypeError:
                    return 0
                except ZeroDivisionError:
                    return 0

    def exponent(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = self.stack.pop()
                    _b = self.stack.pop()
                    self.stack.append(_b ** _a)
                except TypeError:
                    return 0

    def square(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(_a ** 2)
                except TypeError:
                    return 0

    def greater_than(self):
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
                    return 0

    def less_than(self):
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
                    return 0

    def comparison(self):
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
                    return 0

    def absolute_value(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(abs(_a))
                except TypeError:
                    return 0

    def replace(self):
        if len(self.stack) >= 1:
            if self.stack_var != '':
                self.stack.pop()
                self.stack.append(self.stack_var)
                self.stack_var = ''

    def factorial(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                try:
                    _a = self.stack.pop()
                    self.stack.append(math.factorial(_a))
                except TypeError:
                    return 0

    def swap(self):
        if len(self.stack) >= 2:
            _a = self.stack[-1]
            _b = self.stack[-2]
            self.stack[-1] = _b
            self.stack[-2] = _a

    def isolate(self):
        if len(self.stack) >= 2:
            self.stack = [self.stack[-1]]

    def reverse(self):
        if len(self.stack) >= 2:
            self.stack = list(reversed(self.stack))

    def capture(self):
        if len(self.stack) >= 1:
            self.stack_var = self.stack.pop()

    def sort(self):
        if len(self.stack) >= 2:
            self.stack = list(sorted(self.stack))

    def to_char(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                self.stack.append(chr(stack.pop()))

    def to_int(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                _a = self.stack.pop()
                self.stack.append(ord(_a))

    def write(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                sys.stdout.write(self.stack[-1])
            else:
                sys.stdout.write(str(self.stack[-1]))

    def print(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], str):
                print(self.stack[-1])
            else:
                print(str(self.stack[-1]))

    def wrap_left(self):
        if len(self.stack) >= 1:
            self.stack = self.stack[1:] + self.stack[:1]

    def wrap_right(self):
        if len(self.stack) >= 1:
            self.stack = self.stack[-1:] + self.stack[:-1]

    def expell_false(self):
        if len(self.stack) >= 1:
            self.stack[:] = [x for x in self.stack if x != 0]

    def repeat(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                for _ in list(range(_a - 1)):
                    try:
                        self.tape.append(self.tape[-1])
                        self.tape_length = len(self.tape)
                    except IndexError:
                        return 0

    def combine(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int) and isinstance(self.stack[-2], int):
                try:
                    _a = stack.pop()
                    _b = stack.pop()
                    self.stack.append(int(str(_b) + str(_a)))
                except TypeError:
                    return 0

    def copy(self):
        if len(self.stack) >= 1:
            self.stack.append(self.stack[-1])

    def expand(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                _exp = range(1, a + 1)
                for i in list(_exp):
                    self.stack.append(i)

    def randomize(self):
        if len(self.stack) >= 2:
            random.shuffle(self.stack)

    def sum_all(self):
        if len(self.stack) >= 1:
            _total = 0
            for i in self.stack:
                if isinstance(i, int):
                    _total += i
            stack = [x for x in self.stack if not isinstance(x, int)]
            stack.append(_total)

    def increment(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                self.stack.append(a + 1)

    def break_apart(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                for i in list(map(int, str(abs(a)))):
                    self.stack.append(i)

    def input(self):
        _a = input()
        try:
            self.stack.append(int(_a))
        except ValueError:
            return 0

    def length(self):
        if len(self.stack) >= 1:
            self.stack.append(len(self.stack))

    def is_even(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                _a = self.stack.pop()
                if _a % 2 == 0:
                    self.stack.append(1)
                else:
                    self.stack.append(0)

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
                self.replace()
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
                self.expell_false()
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
                print("Henlo")
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
                #interpreter.debug()
                interpreter.start()
    else:
        code = sys.argv[1]
        interpreter = Interpreter(code)
        interpreter.start()


if __name__ == "__main__":
    main()
