import pennylane as qml
import numpy as np
import math

dev = qml.device('default.qubit', wires=3)

# rescale input to fit in the range
def rescale(side1,side2,side3,side4):
    divider = math.sqrt(side1**2 + side2**2 + side3**2 + side4**2)
    normalized_arr = []
    normalized_arr.append(np.pi*(side1/divider))
    normalized_arr.append(np.pi*(side2/divider))
    normalized_arr.append(np.pi*(side3/divider))
    normalized_arr.append(np.pi*(side4/divider))
    return normalized_arr

# helper function that solves the problem in classical way
def testfn(side1,side2,side3,side4):
    return side1 == side2 and side3 == side4 or side1 == side3 and side2 == side4 or \
           side1 == side4 and side2 == side3

# performs test on given input using testfn
def test(inputarray):
    for test in inputarray:
        result = is_rectangle(test[0],test[1],test[2],test[3])
        answer = testfn(test[0],test[1],test[2],test[3])
        print(answer, "==", result, ":", answer == result)

@qml.qnode(dev)
def circuit_match_side(side1: int, side2: int) -> list:

    # set up register for cSWAP
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    qml.RY(side1, wires=0)
    qml.RY(side2, wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    # close the register to complete swap test
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

# main function
def is_rectangle(side1: int, side2:int, side3: int, \
                 side4: int) -> bool:

    # normalize input so data encoded remain in [0,pi)
    sides = rescale(side1,side2,side3,side4)
    
    # check if any two sides match
    result1 = circuit_match_side(sides[0],sides[1])
    result2 = circuit_match_side(sides[0],sides[2])
    result3 = circuit_match_side(sides[0],sides[3])
    result4 = circuit_match_side(sides[1],sides[2])
    result5 = circuit_match_side(sides[1],sides[3])
    result6 = circuit_match_side(sides[2],sides[3])

    # return true if two pairs exist in the inputs
    if math.isclose(result1[1], 1) and math.isclose(result6[1], 1):
        return True
    if math.isclose(result2[1], 1) and math.isclose(result5[1], 1):
        return True
    if math.isclose(result3[1], 1) and math.isclose(result4[1], 1):
        return True

    return False


if __name__ == '__main__':
    testarr = [[1,2,2,1]]
    test(testarr)