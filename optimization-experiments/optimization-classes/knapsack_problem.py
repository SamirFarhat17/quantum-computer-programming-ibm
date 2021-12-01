from qiskit_optimization.applications.vertex_cover import VertexCover
import networkx as nx
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit import Aer
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit_optimization.applications import Knapsack

seed = 68
qins = QuantumInstance(backend=Aer.get_backend('qasm_simulator'), shots=1000, seed_simulator=seed, seed_transpiler=seed)

prob = Knapsack(values = [3, 4, 5, 6, 7], weights = [2, 3, 4, 5, 6], max_weight=10)
qp = prob.to_quadratic_program()
print(qp)

# Numpy Eigensolver
meo = MinimumEigenOptimizer(min_eigen_solver=NumPyMinimumEigensolver())
result = meo.solve(qp)
print('result:\n', result)
print('\nsolution:\n', prob.interpret(result))

# QAOA
meo = MinimumEigenOptimizer(min_eigen_solver=QAOA(reps=1, quantum_instance=qins))
result = meo.solve(qp)
print('result:\n', result)
print('\nsolution:\n', prob.interpret(result))
print('\ntime:', result.min_eigen_solver_result.optimizer_time)

from qiskit_optimization.converters import QuadraticProgramToQubo
# the same knapsack problem instance as in the previous section
prob = Knapsack(values = [3, 4, 5, 6, 7], weights = [2, 3, 4, 5, 6], max_weight=10)
qp = prob.to_quadratic_program()
print(qp)

# intermediate QUBO form of the optimization problem
conv = QuadraticProgramToQubo()
qubo = conv.convert(qp)
print(qubo)

# qubit Hamiltonian and offset
op, offset = qubo.to_ising()
print(f'num qubits: {op.num_qubits}, offset: {offset}\n')
print(op)