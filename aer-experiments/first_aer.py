import qiskit
from qiskit.providers.aer import AerSimulator
from qiskit import IBMQ, Aer
provider = IBMQ.load_account()
available_cloud_backends = provider.backends()
print('\nHere is the list of cloud backends that are available to you:')
for i in available_cloud_backends: print(i)

available_local_backends = Aer.backends()
print('\nHere is the list of local backends that are available to you: ')
for i in available_local_backends: print(i)

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

# Construct an ideal simulator
aersim = AerSimulator()

# Perform an ideal simulation
result_ideal = qiskit.execute(circ, aersim).result()
counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)

# Construct a noisy simulator backend from an IBMQ backend
# This simulator backend will be automatically configured
# using the device configuration and noise model

backend = provider.get_backend('ibmq_quito')
aersim_backend = AerSimulator.from_backend(backend)

# Perform noisy simulation
result_noise = qiskit.execute(circ, aersim_backend).result()
counts_noise = result_noise.get_counts(0)

print('Counts(noise):', counts_noise)
# Counts(noise): {'000': 492, '001': 6, '010': 8, '011': 14, '100': 3, '101': 14, '110': 18, '111': 469}
