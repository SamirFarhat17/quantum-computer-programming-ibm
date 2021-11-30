# Converters for quadratic problems
from qiskit_optimization import QuadraticProgram

# Inequality to Equality
qp = QuadraticProgram()
qp.binary_var('x')
qp.binary_var('y')
qp.integer_var(lowerbound=0, upperbound=7, name='z')

qp.maximize(linear={'x': 2, 'y': 1, 'z': 1})
qp.linear_constraint(linear={'x': 1, 'y': 1, 'z': 1}, sense='LE', rhs=5.5,name='xyz_leq')
qp.linear_constraint(linear={'x': 1, 'y': 1, 'z': 1}, sense='GE', rhs=2.5,name='xyz_geq')
#print(qp.export_as_lp_string())
from qiskit_optimization.converters import InequalityToEquality
ineq2eq = InequalityToEquality()
qp_eq = ineq2eq.convert(qp)
#print(qp_eq.export_as_lp_string())

# Integer to Binary
#print(qp_eq.export_as_lp_string())
from qiskit_optimization.converters import IntegerToBinary
int2bin = IntegerToBinary()
qp_eq_bin = int2bin.convert(qp_eq)
#print(qp_eq_bin.export_as_lp_string())

# Linear Equality to Penalty
#print(qp_eq_bin.export_as_lp_string())
from qiskit_optimization.converters import LinearEqualityToPenalty
lineq2penalty = LinearEqualityToPenalty()
qubo = lineq2penalty.convert(qp_eq_bin)
print(qubo.export_as_lp_string())
