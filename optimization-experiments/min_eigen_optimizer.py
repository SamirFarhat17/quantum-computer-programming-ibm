from qiskit import BasicAer
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit_optimization.algorithms import MinimumEigenOptimizer, RecursiveMinimumEigenOptimizer, SolutionSample, OptimizationResultStatus
from qiskit_optimization import QuadraticProgram
from qiskit.visualization import plot_histogram
from typing import List, Tuple
import numpy as np


# Converting QUBO to an operator
qubo = QuadraticProgram()
qubo.binary_var('x')
qubo.binary_var('y')
qubo.binary_var('z')
qubo.minimize(linear=[1,-2,3], quadratic={('x', 'y'): 1, ('x', 'z'): -1, ('y', 'z'): 2})
#print(qubo.export_as_lp_string())

op, offset = qubo.to_ising()
#print('offset: {}'.format(offset))
#print('operator:')
#print(op)

qp=QuadraticProgram()
qp.from_ising(op, offset, linear=True)
#print(qp.export_as_lp_string())

# Solving QUBO with MinEiggenOptimizer
algorithm_globals.random_seed = 10598
quantum_instance = QuantumInstance(BasicAer.get_backend('statevector_simulator'),
                                   seed_simulator=algorithm_globals.random_seed,
                                   seed_transpiler=algorithm_globals.random_seed)
qaoa_mes = QAOA(quantum_instance=quantum_instance, initial_point=[0., 0.])
exact_mes = NumPyMinimumEigensolver()

qaoa = MinimumEigenOptimizer(qaoa_mes)   # using QAOA
exact = MinimumEigenOptimizer(exact_mes)  # using the exact classical numpy minimum eigen solver
exact_result = exact.solve(qubo)
print(exact_result)