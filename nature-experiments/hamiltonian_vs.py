from qiskit_nature.drivers.second_quantization import GaussianForcesDriver

driver = GaussianForcesDriver(
                 ['#p B3LYP/6-31g Freq=(Anharm) Int=Ultrafine SCF=VeryTight',
                  '',
                  'CO2 geometry optimization B3LYP/6-31g',
                  '',
                  '0 1',
                  'C  -0.848629  2.067624  0.160992',
                  'O   0.098816  2.655801 -0.159738',
                  'O  -1.796073  1.479446  0.481721',
                  '',
                  ''])

from qiskit_nature.problems.second_quantization import VibrationalStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import DirectMapper

vibrational_problem = VibrationalStructureProblem(driver, num_modals=2, truncation_order=2)
second_q_ops = vibrational_problem.second_q_ops()

print(second_q_ops[0])


