import networkx as nx
from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization.applications import Clique
from qiskit_optimization.converters import QuadraticProgramToQubo


class CliqueBenchmarks:

    params = ([5, 10, 17, 25], [2, 4, 8, 16])
    param_names = ["number of nodes", "degree"]

    def setup(self, n, d):
        seed = 671
        algorithm_globals.random_seed = seed
        qasm_sim = Aer.get_backend("qasm_simulator")
        self._qins = QuantumInstance(
            backend=qasm_sim, shots=1, seed_simulator=seed, seed_transpiler=seed
        )
        if n >= d:
            graph = nx.random_regular_graph(n=n, d=d)
            self._clique = Clique(graph=graph)
            self._qp = self._clique.to_quadratic_program()
        else:
            raise NotImplementedError

    @staticmethod
    def _generate_qubo(clique: Clique):
        q_p = clique.to_quadratic_program()
        conv = QuadraticProgramToQubo()
        qubo = conv.convert(q_p)
        return qubo

    def time_generate_qubo(self, _, __):
        self._generate_qubo(self._clique)

    def time_qaoa(self, _, __):
        meo = MinimumEigenOptimizer(
            min_eigen_solver=QAOA(reps=1, quantum_instance=self._qins)
        )
        meo.solve(self._qp)
