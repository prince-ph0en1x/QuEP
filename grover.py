"""3 qubit Grover search for 101 state
"""

import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import GradientDescentOptimizer

dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def grover():

    # Create equal superposition
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    for lctr in range(0,k):
        
        # Mark
        #qml.PauliX(wires=0)
        #qml.PauliX(wires=1)
        #qml.PauliX(wires=2)

        qml.Hadamard(wires=2)

        qml.Hadamard(wires=2)
        qml.CNOT(wires=[1,2])
        qml.RZ(-np.pi/4,wires=2) #T_dag
        qml.CNOT(wires=[0,2])
        qml.RZ(np.pi/4,wires=2) #T
        qml.CNOT(wires=[1,2])
        qml.RZ(-np.pi/4,wires=2)
        qml.CNOT(wires=[0,2])
        qml.RZ(np.pi/4,wires=1)
        qml.RZ(np.pi/4,wires=2)
        qml.CNOT(wires=[0,1])
        qml.Hadamard(wires=2)
        qml.RZ(np.pi/4,wires=0)
        qml.RZ(np.pi/4,wires=1)
        qml.CNOT(wires=[0,1])

        qml.Hadamard(wires=2)

        #qml.PauliX(wires=0)
        #qml.PauliX(wires=1)
        #qml.PauliX(wires=2)

        # Amplitude Amplification
        qml.Hadamard(wires=0)
        qml.Hadamard(wires=1)
        qml.Hadamard(wires=2)

        qml.PauliX(wires=0)
        qml.PauliX(wires=1)
        qml.PauliX(wires=2)

        qml.Hadamard(wires=2)

        qml.Hadamard(wires=2)
        qml.CNOT(wires=[1,2])
        qml.RZ(-np.pi/4,wires=2) #T_dag
        qml.CNOT(wires=[0,2])
        qml.RZ(np.pi/4,wires=2) #T
        qml.CNOT(wires=[1,2])
        qml.RZ(-np.pi/4,wires=2)
        qml.CNOT(wires=[0,2])
        qml.RZ(np.pi/4,wires=1)
        qml.RZ(np.pi/4,wires=2)
        qml.CNOT(wires=[0,1])
        qml.Hadamard(wires=2)
        qml.RZ(np.pi/4,wires=0)
        qml.RZ(np.pi/4,wires=1)
        qml.CNOT(wires=[0,1])

        qml.Hadamard(wires=2)

        qml.PauliX(wires=0)
        qml.PauliX(wires=1)
        qml.PauliX(wires=2)

        qml.Hadamard(wires=0)
        qml.Hadamard(wires=1)
        qml.Hadamard(wires=2)
    

    return (qml.expval.PauliZ(0),qml.expval.PauliZ(1),qml.expval.PauliZ(2))

# |0⟩ state expectation value in PauliZ is +1
# (|0⟩+|1⟩)/sqrt(2) state expectation value in PauliZ is 0
# |1⟩ state expectation value in PauliZ is -1

#k = 1
#print("Iter = 1")
#grover()
#sv = dev._state
#for i in sv:
#    print(abs(i))
#
#k = 2
#print("Iter = 2")
#grover()
#sv = dev._state
#for i in sv:
#    print(abs(i))

k = 2
print("Iter = ",k)
grover()
sv = dev._state
for i in sv:
    print(i,abs(i))