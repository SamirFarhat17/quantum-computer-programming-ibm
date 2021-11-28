from qiskit.chemistry.drivers import PySCFDriver, UnitsType, Molecule
from qiskit.chemistry.transformations import FermionicTransformation, FermionicQubitMappingType

molecule = Molecule(geometry=[['H', [0., 0., 0.]],
                              ['H', [0., 0., 0.735]]],
                     charge=0, multiplicity=1)
driver = PySCFDriver(molecule = molecule, unit=UnitsType.ANGSTROM, basis='sto3g')
transformation = FermionicTransformation(qubit_mapping=FermionicQubitMappingType.JORDAN_WIGNER)

from qiskit.chemistry.algorithms import NumPyEigensolverFactory

numpy_solver = NumPyEigensolverFactory(use_default_filter_criterion=True)

from qiskit import BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.chemistry.algorithms.ground_state_solvers import (GroundStateEigensolver,
                                                              VQEUCCSDFactory)
from qiskit.chemistry.algorithms.excited_states_solvers import QEOM

# This first part sets the ground state solver
# see more about this part in the ground state calculation tutorial
quantum_instance = QuantumInstance(BasicAer.get_backend('statevector_simulator'))
solver = VQEUCCSDFactory(quantum_instance)
gsc = GroundStateEigensolver(transformation, solver)

# The qEOM algorithm is simply instantiated with the chosen ground state solver
qeom_excited_states_calculation = QEOM(gsc, 'sd')


from qiskit.chemistry.algorithms.excited_states_solvers import ExcitedStatesEigensolver

numpy_excited_states_calculation = ExcitedStatesEigensolver(transformation, numpy_solver)
numpy_results = numpy_excited_states_calculation.solve(driver)

qeom_results = qeom_excited_states_calculation.solve(driver)

'''print(numpy_results)
print('\n\n')
print(qeom_results)'''


import numpy as np

def filter_criterion(eigenstate, eigenvalue, aux_values):
    return np.isclose(aux_values[0][0], 2.)

new_numpy_solver = NumPyEigensolverFactory(filter_criterion=filter_criterion)
new_numpy_excited_states_calculation = ExcitedStatesEigensolver(transformation, new_numpy_solver)
new_numpy_results = new_numpy_excited_states_calculation.solve(driver)

print(new_numpy_results)