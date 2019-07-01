"""Test Toffoli Gate
"""

import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import GradientDescentOptimizer

dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def formQcirc():
    prepz()
    toffoli()
    return meas()

def prepz():
    # |00⟩ -->  +1.0
    
    # |01⟩ -->  +1.0
    #qml.PauliX(wires=0)
    
    # |10⟩ -->  +1.0
    #qml.PauliX(wires=1)
    
    # |11⟩ -->  -1.0
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)

def toffoli():
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

def meas():
    return (qml.expval.PauliZ(2))

print(formQcirc())