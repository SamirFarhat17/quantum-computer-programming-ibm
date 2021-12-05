
from qiskit.circuit.library import IntegerComparator, WeightedAdder, QuadraticForm

from benchmark.simulator_benchmark import SimulatorBenchmarkSuite
from benchmark.basic import BasicSimulatorBenchmarkSuite

DEFAULT_QUBITS = [ 25 ]

DEFAULT_RUNTIME = [
    SimulatorBenchmarkSuite.RUNTIME_STATEVECTOR_CPU,
    ]

DEFAULT_MEASUREMENT_METHODS = [
    SimulatorBenchmarkSuite.MEASUREMENT_SAMPLING
    ]

DEFAULT_MEASUREMENT_COUNTS = SimulatorBenchmarkSuite.DEFAULT_MEASUREMENT_COUNTS

DEFAULT_NOISE_MODELS = [
    SimulatorBenchmarkSuite.NOISE_IDEAL
]


class ArithmeticCircuits(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if apps is None:
            apps = {
                'integer_comparator': 10,
                'weighted_adder': 1,
                'quadratic_form': 10,
                'draper_qft_adder': 10,
                'cdkm_ripple_carry_adder':10,
                'vbe_ripple_carry_adder': 10,
                'hrs_cum_mult': 10,
                'rgqft_mult': 10
            }
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME

        super().__init__('arithmetic_circuits',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class BasicChangeCircuits(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = {'qft': 1}
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS

        super().__init__('basic_change_circuits',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class NLocalCircuits(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = {
                'real_amplitudes': 10,
                'real_amplitudes_linear': 10,
                'efficient_su2': 10,
                'efficient_su2_linear': 10,
                'excitation_preserving': 10,
                'excitation_preserving_linear': 10
            }

        super().__init__('n_local_circuits',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class ParticularQuantumCircuits(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = {
                'fourier_checking': 10,
                'graph_state': 10,
                'hidden_linear_function': 10,
                'iqp': 10,
                'quantum_volume': 1,
                'phase_estimation': 1
            }

        super().__init__('particular_quantum_circuits',
                         apps, qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class ProbabilityDistributionCircuits(BasicSimulatorBenchmarkSuite):
    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = {
                'uniform_distribution': 10,
                'normal_distribution': 10,
                'log_normal_distribution': 10,
            }

        super().__init__('probability_distribution_circuits',
                         apps, qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class StandardGates(BasicSimulatorBenchmarkSuite):
    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = {
                'barrier': 10,
                'mc_phase': 10,
            }

        super().__init__('standard_gates',
                         apps, qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class PauliRotationCircuits(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if apps is None:
            apps = {
                'linear_pauli_rotations': 10,
                'poly_pauli_rotations': 10,
                'piecewise_lin_pauli_rotations': 10,
                'piecewise_poly_pauli_rotations': 10,
            }
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME

        super().__init__('pauli_rotations',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


class GeneralizedGates(BasicSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=DEFAULT_MEASUREMENT_COUNTS,
                 noise_model_names=None):
        if apps is None:
            apps = {
                'mcmt': 10,
                'mcmtv_chain': 10,
                'permutation': 10,
                'gms': 10,
                'gr': 10,
                'grx': 10,
                'gry': 10,
                'grz': 10
            }
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME

        super().__init__('generalized_gates',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


if __name__ == "__main__":
    benchmarks = [ArithmeticCircuits(), BasicChangeCircuits(), NLocalCircuits(), ParticularQuantumCircuits(),
                  ProbabilityDistributionCircuits(), StandardGates(), PauliRotationCircuits(), GeneralizedGates()]
    for benchmark in benchmarks:
        benchmark.run_manual()
