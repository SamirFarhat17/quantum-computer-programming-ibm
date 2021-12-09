import time
from typing import List, Optional, Any
import numpy as np
import matplotlib.pyplot as plt

from docplex.mp.model import Model

from qiskit import BasicAer, Aer
from qiskit.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit_optimization.algorithms import CobylaOptimizer, MinimumEigenOptimizer
from qiskit_optimization.problems import QuadraticProgram
from qiskit_optimization.algorithms.admm_optimizer import ADMMParameters, ADMMOptimizer
from qiskit_optimization.translators import from_docplex_mp


class Admm3Benchmarks:
    params = ([2, 3, 4, 5], [2, 4, 8, 16])
    param_names = ["number of items", "max_weights"]

    def setup(self):
        # construct model using docplex
        mdl = Model('ex6')

        v = mdl.binary_var(name='v')
        w = mdl.binary_var(name='w')
        t = mdl.binary_var(name='t')
        u = mdl.continuous_var(name='u')

        mdl.minimize(v + w + t + 5 * (u - 2) ** 2)
        mdl.add_constraint(v + 2 * w + t + u <= 3, "cons1")
        mdl.add_constraint(v + w + t >= 1, "cons2")
        mdl.add_constraint(v + w == 1, "cons3")

        # load quadratic program from docplex model
        self._qp = from_docplex_mp(mdl)

        # define COBYLA optimizer to handle convex continuous problems.
        cobyla = CobylaOptimizer()

        qaoa = MinimumEigenOptimizer(QAOA(quantum_instance=Aer.get_backend('qasm_simulator')))

        # define QUBO optimizer
        qubo_optimizer = qaoa

        # define classical optimizer
        convex_optimizer = cobyla

        admm_params = ADMMParameters(
            rho_initial=1001,
            beta=1000,
            factor_c=900,
            maxiter=100,
            three_block=True, tol=1.e-6
        )

        # initialize ADMM with classical QUBO and convex optimizer
        self._admm_q = ADMMOptimizer(params=admm_params,
                                     qubo_optimizer=qubo_optimizer,
                                     continuous_optimizer=convex_optimizer)

    def time_admm(self, _, __):
        # construct model using docplex
        mdl = Model('ex6')

        v = mdl.binary_var(name='v')
        w = mdl.binary_var(name='w')
        t = mdl.binary_var(name='t')
        u = mdl.continuous_var(name='u')

        mdl.minimize(v + w + t + 5 * (u - 2) ** 2)
        mdl.add_constraint(v + 2 * w + t + u <= 3, "cons1")
        mdl.add_constraint(v + w + t >= 1, "cons2")
        mdl.add_constraint(v + w == 1, "cons3")

        # load quadratic program from docplex model
        qp = from_docplex_mp(mdl)
        # define COBYLA optimizer to handle convex continuous problems.
        cobyla = CobylaOptimizer()

        qaoa = MinimumEigenOptimizer(QAOA(quantum_instance=Aer.get_backend('qasm_simulator')))

        # define QUBO optimizer
        qubo_optimizer = qaoa

        # define classical optimizer
        convex_optimizer = cobyla

        admm_params = ADMMParameters(
            rho_initial=1001,
            beta=1000,
            factor_c=900,
            maxiter=100,
            three_block=True, tol=1.e-6
        )

        # define QUBO optimizer
        qubo_optimizer = qaoa

        # define classical optimizer
        convex_optimizer = cobyla
        # convex_optimizer = cplex  # uncomment to use CPLEX instead

        # initialize ADMM with quantum QUBO optimizer and classical convex optimizer
        admm_q = ADMMOptimizer(params=admm_params,
                               qubo_optimizer=qubo_optimizer,
                               continuous_optimizer=convex_optimizer)
        # run ADMM to solve problem
        result_q = admm_q.solve(qp)
