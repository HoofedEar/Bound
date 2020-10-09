# Bound
Stack-based esolang involving integers

| Command | Function                                                                   | Example                             |
|---------|----------------------------------------------------------------------------|-------------------------------------|
| `i`       | Get input from the user, add to stack. (Raw input)                         | `i "hello"` becomes ["hello"]         |
| `+`       | Sum of the top two elements.                                               | `2 2 +` becomes [4]                   |
| `-`       | Subtract the top element from the second top element.                      | `3 2 -` becomes [1]                   |
| `*`       | Multiply the top two elements together.                                    | `5 3 *` becomes [15]                  |
| `/`       | Divide the second top element by the top element, rounded up.              | `4 3 /` becomes [2]                   |
| `\`       | Divide the second top element by the top element, rounded down.            | `4 3 \` becomes [1]                   |
| `%`       | Modulo with the top two elements.                                          | `5 3 %` becomes [2]                   |
| `^`       | Multiply the second element to the power of the top element.               | `2 9 ^` becomes [512]                 |
| `#`       | Square the top element.                                                    | `6 5 #` becomes [6, 25]               |
| `>`       | Greater than involving the top two elements. (0=False,1=True)              | `2 3 >` becomes [0]                   |
| `<`       | Less than involving the top two elements.                                  | `2 3 <` becomes [1]                   |
| `=`       | Integer comparison with top two elements.                                  | `3 3 =` becomes [1]                   |
| `\|`      | Absolute value of the top most element.                                    | `2 3 - \|` becomes [1]                |
| `g`       | Pop the top value and store it.                                            | `5 3 2 g` becomes [5, 3]              |
| `G`       | Replace the top value with the stored element, if there is a stored value. | `5 3 2 g 1 G` becomes [5, 3, 2]       |
| `;`       | Swap the top two elements.                                                 | `1 7 ;` becomes [7, 1]                |
| `,`       | Remove all but the top element.                                            | `1 2 3 4 5 ,` becomes [5]             |
| `l`       | Length of string at top element.                                           | `i "hello" l` becomes [5]             |
| `@`       | Reverses the stack.                                                        | `1 2 3 @` becomes [3, 2, 1]           |
| `$`       | Sort the stack.                                                            | `3 1 2 $` becomes [1, 2, 3]           |
| `d`       | Convert the top integer into a char.                                       | `9 1 + 6 * 5 + d` becomes ['A']       |
| `'`       | The next char is converted into an integer.                                | `' a` becomes [97]                    |
| `s`       | Write each char in the stack out to stdout.                                | `9 1 + 6 * 5 + s` outputs 'A'         |
| `{`       | Rotates the top element to the left.                                       | `1 2 3 4 {` becomes [2, 3, 4, 1]      |
| `}`       | Rotates the top element to the right.                                      | `1 2 3 4 }` becomes [4, 1, 2, 3]      |
| `U`       | Removes all falsey elements from the stack.                                | `2 3 > U 7` becomes [7]               |
| `R`       | Repeats the next command n times, where n is top value.                    | `2 2 2 3 R +` becomes [6]             |
