import numpy as np
from qiskit import Aer, QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit.opflow import StateFn, PauliSumOp, AerPauliExpectation, ListOp, Gradient
from qiskit.utils import QuantumInstance

# set method to calculcate expected values
expval = AerPauliExpectation()

# define gradient method
gradient = Gradient()

# define quantum instances (statevector and sample based)
qi_sv = QuantumInstance(Aer.get_backend('aer_simulator_statevector'))

# we set shots to 10 as this will determine the number of samples later on.
qi_qasm = QuantumInstance(Aer.get_backend('aer_simulator'), shots=10)

from qiskit_machine_learning.neural_networks import OpflowQNN
# construct parametrized circuit
params1 = [Parameter('input1'), Parameter('weight1')]
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.ry(params1[0], 0)
qc1.rx(params1[1], 0)
qc_sfn1 = StateFn(qc1)

# construct cost operator
H1 = StateFn(PauliSumOp.from_list([('Z', 1.0), ('X', 1.0)]))

# combine operator and circuit to objective function
op1 = ~H1 @ qc_sfn1
print(op1)

# construct OpflowQNN with the operator, the input parameters, the weight parameters,
# the expected value, gradient, and quantum instance.
qnn1 = OpflowQNN(op1, [params1[0]], [params1[1]], expval, gradient, qi_sv)
# define (random) input and weights
input1 = np.random.rand(qnn1.num_inputs)
weights1 = np.random.rand(qnn1.num_weights)
# QNN forward pass
qnn1.forward(input1, weights1)
# QNN batched forward pass
qnn1.forward([input1, input1], weights1)
# QNN backward pass
qnn1.backward(input1, weights1)
# QNN batched backward pass
qnn1.backward([input1, input1], weights1)
op2 = ListOp([op1, op1])
qnn2 = OpflowQNN(op2, [params1[0]], [params1[1]], expval, gradient, qi_sv)
# QNN forward pass
qnn2.forward(input1, weights1)
# QNN backward pass
qnn2.backward(input1, weights1)

from qiskit_machine_learning.neural_networks import TwoLayerQNN
# specify the number of qubits
num_qubits = 3
# specify the feature map
fm = ZZFeatureMap(num_qubits, reps=2)
fm.draw(output='mpl')
# specify the ansatz
ansatz = RealAmplitudes(num_qubits, reps=1)
ansatz.draw(output='mpl')
# specify the observable
observable = PauliSumOp.from_list([('Z'*num_qubits, 1)])
print("Two layer QNN observable: " + str(observable))
# define two layer QNN
qnn3 = TwoLayerQNN(num_qubits,
                   feature_map=fm,
                   ansatz=ansatz,
                   observable=observable, quantum_instance=qi_sv)
# define (random) input and weights
input3 = np.random.rand(qnn3.num_inputs)
weights3 = np.random.rand(qnn3.num_weights)
# QNN forward pass
qnn3.forward(input3, weights3)
# QNN backward pass
qnn3.backward(input3, weights3)

# Circuit QNN
from qiskit_machine_learning.neural_networks import CircuitQNN
qc = RealAmplitudes(num_qubits, entanglement='linear', reps=1)
qc.draw(output='mpl')
# specify circuit QNN
qnn4 = CircuitQNN(qc, [], qc.parameters, sparse=True, quantum_instance=qi_qasm)
# define (random) input and weights
input4 = np.random.rand(qnn4.num_inputs)
weights4 = np.random.rand(qnn4.num_weights)
# QNN forward pass
qnn4.forward(input4, weights4).todense()  # returned as a sparse matrix
qnn4.backward(input4, weights4)
# specify circuit QNN
parity = lambda x: '{:b}'.format(x).count('1') % 2
output_shape = 2  # this is required in case of a callable with dense output
qnn6 = CircuitQNN(qc, [], qc.parameters, sparse=False, interpret=parity, output_shape=output_shape,
                  quantum_instance=qi_qasm)
# define (random) input and weights
input6 = np.random.rand(qnn6.num_inputs)
weights6 = np.random.rand(qnn6.num_weights)
# QNN forward pass
qnn6.forward(input6, weights6)
# QNN backward pass
qnn6.backward(input6, weights6)
# specify circuit QNN
qnn7 = CircuitQNN(qc, [], qc.parameters, sampling=True,
                  quantum_instance=qi_qasm)
# define (random) input and weights
input7 = np.random.rand(qnn7.num_inputs)
weights7 = np.random.rand(qnn7.num_weights)
# QNN forward pass, results in samples of measured bit strings mapped to integers
qnn7.forward(input7, weights7)
# QNN backward pass
qnn7.backward(input7, weights7)
# specify circuit QNN
qnn8 = CircuitQNN(qc, [], qc.parameters, sampling=True, interpret=parity,
                  quantum_instance=qi_qasm)
# define (random) input and weights
input8 = np.random.rand(qnn8.num_inputs)
weights8 = np.random.rand(qnn8.num_weights)
# QNN forward pass, results in samples of measured bit strings
qnn8.forward(input8, weights8)
# QNN backward pass
qnn8.backward(input8, weights8)