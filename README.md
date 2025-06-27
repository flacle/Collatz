# Collatz 2-Adic Parity Map
Clockwise arc diagram visualization of the parity reformulation of the Collatz function.
<br />&nbsp;<br />
![Clockwise arc diagram of orbits from the parity Collatz function for n0=25](https://github.com/flacle/Collatz/blob/main/n_0_25.svg?raw=true)
*This example shows the orbit of the parity map 25 -> 38 -> 19 -> 44 -> 11 -> 26 -> 13 -> 20 -> 5 -> 8 -> 1.*
## Features
1. Show or hide differences between increments or decrements of n_{t} - n_{t-1} (edgeLabels = True/False)
1. Show or hide nodes on the number line (hideNodes = True/False)
2. Diagrams can be saved/displayed as either SVGs or PNGs

## General Info
1. Language: Python 3
1. Dependencies:
   1. mpmath
   1. math
   1. drawSvg
   1. functools

## License
This project is licensed under the terms of the [MIT license](https://github.com/flacle/Collatz/blob/main/LICENSE).
