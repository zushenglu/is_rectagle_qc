
# is_rectangle


A small python program that takes 4 positive integers and returns True if a rectangle with the same side lengths as the inputs can be formed.



The program uses Pennylane Library, Numpy and the standard math library.

The solution is procured by embedding inputs to qubits and checking them using the Swap test. Results are matched to produce the final output.

    
## Functions

`is_rectangle(side1, side2, side3, side4):` Main function, takes 4 positive integers and returns True if a rectangle with same side lengths can be constructed, 0 excluded.




`circuit_match_side(side1: int, side2: int):` Builds a quantum circuit and returns an array of the probability of two equal inputs. index 0 for inequality, and 1 for equality

`test(list[list[4]]):` helper function for testing, takes a list of inputs and prints the result
