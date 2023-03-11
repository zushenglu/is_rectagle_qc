import math
import pennylane as qml
import numpy as np
dev = qml.device('default.qubit', wires=14)
dev2 = qml.device('default.qubit', wires=14)
dev3 = qml.device('default.qubit', wires=14)
dev4 = qml.device('default.qubit', wires=14)
dev5 = qml.device('default.qubit', wires=14)
dev6 = qml.device('default.qubit', wires=14)




@qml.qnode(dev)
def circuit(side):

    # set up register for cSWAP
    for i in range(4,8):
        qml.PauliX(wires=i)
        qml.Hadamard(wires=i)

    # emcode side length data into qubits
    for i in range(4):
        qml.Hadamard(wires=i)
        qml.RY(side[i], wires=i)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[4,2,3])
    qml.CSWAP(wires=[5,0,1])
    qml.CSWAP(wires=[6,1,2])
    qml.CSWAP(wires=[7,0,3])

    # complete register for swap test
    for i in range(4):
        qml.Hadamard(wires=i+4)

    # check if match exist
    qml.Toffoli(wires=[4,5,8])
    qml.Toffoli(wires=[6,7,9])

    # output result to measured qubit
    qml.CNOT(wires=[8,10])
    qml.CNOT(wires=[9,10])
    qml.Toffoli(wires=[8,9,10])

    qml.PauliX(wires=13)
    qml.Hadamard(wires=11)
    qml.Hadamard(wires=12)
    qml.Hadamard(wires=13)
    qml.RY(0.99, wires=11)
    qml.RY(0.99, wires=12)
    # qml.Hadamard(wires=11)
    # qml.Hadamard(wires=12)


    qml.CSWAP(wires=[13,11,12])
    qml.Hadamard(wires=13)


    return qml.probs(wires=2)
 
@qml.qnode(dev2)
def circuit_side1_2(side):

    # set up register for cSWAP

    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[0], wires=0)
    qml.RY(side[1], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

@qml.qnode(dev3)
def circuit_side1_3(side):

    # set up register for cSWAP

    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[0], wires=0)
    qml.RY(side[2], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

@qml.qnode(dev4)
def circuit_side1_4(side):

    # set up register for cSWAP
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[0], wires=0)
    qml.RY(side[3], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

@qml.qnode(dev5)
def circuit_side2_3(side):

    # set up register for cSWAP
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[1], wires=0)
    qml.RY(side[2], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

@qml.qnode(dev5)
def circuit_side2_4(side):

    # set up register for cSWAP
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[1], wires=0)
    qml.RY(side[3], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)

@qml.qnode(dev6)
def circuit_side3_4(side):

    # set up register for cSWAP
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # emcode side length data into qubits
    # qml.Hadamard(wires=0)
    qml.RY(side[2], wires=0)
    qml.RY(side[3], wires=1)

    # check if input matches using cSWAP gate
    qml.CSWAP(wires=[2,0,1])
 
    qml.Hadamard(wires=2)

    return qml.probs(wires=2)



# return an normalized array of given value scaled to pi
def rescale(side1,side2,side3,side4):
    divider = math.sqrt(side1**2 + side2**2 + side3**2 + side4**2)
    normalized_arr = []
    normalized_arr.append(np.pi*(side1/divider))
    normalized_arr.append(np.pi*(side2/divider))
    normalized_arr.append(np.pi*(side3/divider))
    normalized_arr.append(np.pi*(side4/divider))
    return normalized_arr

def isRect(side1, side2, side3, side4):
    
    # given input to be positive integer, so assume smallest
    # input = 1

    # normalize input so data encoded remain in [0,pi)
    sides = rescale(side1,side2,side3,side4)
    
    
    result1 = circuit_side1_2(sides)
    result2 = circuit_side1_3(sides)
    result3 = circuit_side1_4(sides)
    result4 = circuit_side2_3(sides)
    result5 = circuit_side2_4(sides)
    result6 = circuit_side3_4(sides)

    arr = [result1,result2,result3,result4,result5,result6]
    # print(arr)

    if math.isclose(result1[1], 1) and math.isclose(result6[1], 1):
        return True
    if math.isclose(result2[1], 1) and math.isclose(result5[1], 1):
        return True
    if math.isclose(result3[1], 1) and math.isclose(result4[1], 1):
        return True

    return False

def testfn(side1,side2,side3,side4):
    return side1 == side2 and side3 == side4 or side1 == side3 and side2 == side4 or \
           side1 == side4 and side2 == side3

def test(inputarray):
    for test in inputarray:
        result = isRect(test[0],test[1],test[2],test[3])
        answer = testfn(test[0],test[1],test[2],test[3])
        print(answer, "==", result, ":", answer == result)

if __name__ == '__main__':
    testarr = [[1,2,2,1],[1,1,2,2],[1,2,1,2],[1,1,1,1],[1,2,3,4],[1,2,2,3],\
            [5,7,7,5],[4,4,6,6],[7,1,7,1],[4,4,4,4],[4,4,7,8],[7,1,1,7],\
            [3,7,7,3],[3,3,9,9],[1,7,1,7],[9,9,9,9],[34,21,34,21],\
            [7,3,3,7],[9,9,3,3],[2,3,1,4],[109,2,30,4],\
            [2,3,4,1],[9,9,45,45],\
            [np.pi, 2*np.pi, 2*np.pi, np.pi],
            [np.pi, np.pi, 2*np.pi, 2*np.pi],
            [np.pi, 2*np.pi, 2*np.pi, np.pi],
            ]
    

    # test=[[4,4,7,8]]

    # test=[[1,2,3,4],[1,2,3,3]]

    test(testarr)

    # for ti in test:
    #     result = isRect(ti[0],ti[1],ti[2],ti[3])
    #     answer = testfn(ti[0],ti[1],ti[2],ti[3])
    #     print(answer, "==", result, ":", answer == result)
        # print(qml.draw(isRect)(ti[0],ti[1],ti[2],ti[3]))