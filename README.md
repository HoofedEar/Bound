# βound  
[![CodeFactor](https://www.codefactor.io/repository/github/hoofedear/bound/badge/main)](https://www.codefactor.io/repository/github/hoofedear/bound/overview/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
Stack-based interpreted esolang involving integers and single char commands. Inspired by Stuck.    

  
## Usage
`python3 bound.py`  
`python3 bound.py [commands]`  
  
## Command List

| Command | Function                                                                     | Example                               |
|-----------|----------------------------------------------------------------------------|---------------------------------------|
| `0`-`9`   | Puts the integer on top of the stack.                                      | `1 4 5` becomes [1, 4, 5]             |
| `+`       | Sum of the top two elements.                                               | `2 2 +` becomes [4]                   |
| `-`       | Subtract the top element from the second top element.                      | `3 2 -` becomes [1]                   |
| `*`       | Multiply the top two elements together.                                    | `5 3 *` becomes [15]                  |
| `/`       | Divide the second top element by the top element, rounded up.              | `4 3 /` becomes [2]                   |
| `\`       | Divide the second top element by the top element, rounded down.            | `4 3 \` becomes [1]                   |
| `%`       | Modulo with the top two elements.                                          | `5 3 %` becomes [2]                   |
| `^`       | Multiply the second element to the power of the top element.               | `2 9 ^` becomes [512]                 |
| `#`       | Square the top element.                                                    | `6 5 #` becomes [6, 25]               |
| `!`       | Factorial the top element.                                                 | `5 !` becomes [120]                   |
| `>`       | Greater than involving the top two elements. (0=False,1=True)              | `2 3 >` becomes [0]                   |
| `<`       | Less than involving the top two elements.                                  | `2 3 <` becomes [1]                   |
| `=`       | Integer comparison with top two elements.                                  | `3 3 =` becomes [1]                   |
| `\|`      | Absolute value of the top most element.                                    | `2 3 - \|` becomes [1]                |
| `g`       | Pop the top value and store it.                                            | `5 3 2 g` becomes [5, 3]              |
| `G`       | Add to the top of the stack the stored element, if it exists.              | `7 2 g 8 G` becomes [7, 8, 2]            |
| `;`       | Swap the top two elements.                                                 | `1 7 ;` becomes [7, 1]                |
| `,`       | Remove all but the top element.                                            | `1 2 3 4 5 ,` becomes [5]             |
| `@`       | Reverses the stack.                                                        | `1 2 3 @` becomes [3, 2, 1]           |
| `$`       | Sort the stack.                                                            | `3 1 2 $` becomes [1, 2, 3]           |
| `d`       | Convert the top integer into a char.                                       | `9 7 : d` becomes ['a']               |
| `'`       | The top element is converted into an integer, if char.                     | `9 7 : d c '` becomes ['a', 97]       |
| `s`       | Writes out the top element in the stack to stdout.                         | `9 1 : 6 + d s` outputs 'a'           |
| `S`       | Writes out the top element in the stack to stdout, with newline.           | `9 1 : 6 + d S` outputs 'a\n'         |
| `{`       | Rotates the top element to the left.                                       | `1 2 3 {` becomes [2, 3, 1]           |
| `}`       | Rotates the top element to the right.                                      | `1 2 3 }` becomes [3, 1, 2]           |
| `U`       | Removes all falsey elements from the stack.                                | `2 3 > U 7` becomes [7]               |
| `R`       | Repeats the next command n times, where n is top value.                    | `2 2 2 3 R +` becomes [6]             |
| `:`       | Combines the top two values into one if they are both ints.                | `2 2 :` becomes [22]                  |
| `c`       | Puts a copy of the top element onto the stack.                             | `4 3 c c` becomes [4, 3, 3, 3]        |
| `&`       | Puts elements 1 to n onto the stack, exclusively.                          | `5 &` becomes [1, 2, 3, 4, 5]         |
| `~`       | Randomizes the stack.                                                      |                                       |
| `n`       | Sums all ints in the stack together.                                       | `5 5 5 n` becomes [15]                |
| `I`       | Increments the top element of the stack.                                   | `0 I I` becomes [2]                   |
| `D`       | Decrements the top element of the stack.                                   | `7 D D` becomes [5]                   |
| `?`       | Checks if the top element is even. (Lazy modulo)                           | `4 ?` becomes [1]                     | 
| `b`       | Splits the top element into seprate integers                               | `6 ! b` becomes [7, 2, 0]             |
| `i`       | Gets input and puts it to the stack if its an int                          |                                       |
| `_`       | Puts the total number of elements onto the stack.                          | `9 1 2 _` becomes [9, 1, 1, 3]        | 
| `.`       | Toggles output of stack at end of execution.                               | `1 2 3 .` prints [1, 2, 3]            |  
  
  `10:c42:d*@RS`
