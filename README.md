
# is_rectangle

A small python program that takes 4 positive integers and return True if a rectangle with same side lengths as the inputs can be formed.

The program uses Pennylane Library as well as Numpy and the standerd math library. 

Solution is procured by embedding inputs to qubits and checking them using swap test. Results are matched to produce final output. 




    
    
## Functions

**is_rectangle(side1, side2, side3, side4):** Main function, takes 4 positive integers and return True if a rectangle with same side lengths can be constructed, 0 not included.

**circuit_match_side(side1: int, side2: int):** Builds a quantum circuit and returns an array of probability of two inputs being equal. index 0 for inequality, and 1 for equality

**test(list[list[4]]):** helper function for testing, takes a list of inputs and prints the result